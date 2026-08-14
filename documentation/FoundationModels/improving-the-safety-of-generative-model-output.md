# Improving the safety of generative model output

**Framework**: Foundation Models

Create generative experiences that appropriately handle sensitive inputs and respect people.

#### Overview

Generative AI models have powerful creativity, but with this creativity comes the risk of unintended or unexpected results. For any generative AI feature, safety needs to be an essential part of your design.

The Foundation Models framework has two base layers of safety, where the framework uses:

- Apple Foundation Models, running on-device and on Private Cloud Compute, trained to handle sensitive topics with care.
- Guardrails that aim to block harmful or sensitive content, such as self-harm, violence, and adult materials.

Because safety risks are often contextual, some harms might bypass both built-in framework safety layers. It’s vital to consider whether to design additional safety layers specific to your app. When developing your feature, decide what’s acceptable or might be harmful in your generative AI feature, based on your app’s use case, cultural context, and audience.

For more information on designing generative AI experiences responsibly, see Human Interface Guidelines > Foundations > [`Generative AI`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/generative-ai).

#### Review Guardrails for a Model

Guardrails are a safety system tied to a specific model. For example, all on-device Apple Foundation Models you use through [`SystemLanguageModel`](systemlanguagemodel.md) have guardrails that check the input prompt and the model’s output. Use [`SystemLanguageModel.Guardrails`](systemlanguagemodel/guardrails.md) to configure the guardrail level most appropriate for your use case. The Apple Foundation Models on Private Cloud Compute (PCC) also have guardrails, but they have different policies that you can’t directly configure.

For any foundation model you use, consider the following questions early when designing your feature:

- Does the model have a guardrail system? If so, are they configurable?
- When does the model throw errors like [`LanguageModelError.guardrailViolation(_:)`](languagemodelerror/guardrailviolation(_:).md) or [`LanguageModelError.refusal(_:)`](languagemodelerror/refusal(_:).md)?
- When might this model respond with a refusal message such as *“Sorry I cannot help…”*?

Additionally, consider the following questions for your use case and audience:

- Where might the model or its guardrails be too permissive? This is where you need to design additional layers of protection specific to your app.
- Where might the model or its guardrails be too restrictive? This is where you need to work with the model’s guardrail configurations, if any exist, or design your feature to better fit within the model’s policy to provide a better user experience.

#### Handle Guardrail Errors

When you send a prompt to the model, the input prompt and the model output are both checked by a guardrail. If either fails the safety check, the model session throws a [`LanguageModelError.guardrailViolation(_:)`](languagemodelerror/guardrailviolation(_:).md) error:

```swift
do {
    let session = LanguageModelSession()
    let topic = "" // A potentially sensitive topic.
    let prompt = "Write a respectful and funny story about \(topic)."
    let response = try await session.respond(to: prompt)
} catch LanguageModelError.guardrailViolation(let violation) {
    // Handle the safety error.
}
```

If you encounter a guardrail violation error for any built-in prompt in your app, experiment with re-phrasing the prompt to determine which phrases are activating the guardrails, and avoid those phrases. If the error is thrown in response to a prompt created by someone using your app, give people a clear message that explains the issue. For example, you might say “Sorry, this feature isn’t designed to handle that kind of input” and offer people the opportunity to try a different prompt.

#### Handle Model Refusals

A model can freely refuse to respond to an input. For example, the on-device [`SystemLanguageModel`](systemlanguagemodel.md) isn’t suitable for all topics, and it may refuse to discuss sensitive subjects. When you generate a string response and the model refuses a request, it generates a message that might begin with a refusal like *“Sorry, I can’t help with that…”*.

Design your app experience with refusal messages in mind and present the message to the person using your app. You might not be able to programmatically determine whether a string response is a normal response or a refusal, so design the experience to anticipate both. If it’s critical to determine whether the response is a refusal message, initialize a new [`LanguageModelSession`](languagemodelsession.md) and prompt the model to classify whether the string is a refusal.

When you use guided generation to generate Swift structures or types, there’s no placeholder for a refusal message. Instead, the model throws a [`LanguageModelError.refusal(_:)`](languagemodelerror/refusal(_:).md) error. When you catch the error, ask the model to generate a string refusal message:

```swift
do {
    let session = LanguageModelSession()
    let topic = ""  // A sensitive topic.
    let response = try await session.respond(
        to: "List five key points about: \(topic)",
        generating: [String].self
    )
} catch LanguageModelError.refusal(let refusal) {
    do {
        // Attempt to retrieve an explanation for the refusal.
        let explanation = try await refusal.explanation.content
    } catch {
        // The explanation request may fail, so fall back to the debug text.
        let explanation = refusal.debugDescription
    }
}
```

Display the explanation in your app to tell people why a request failed, and offer people the opportunity to try a different prompt. Retrieving an explanation message is asynchronous and takes time for the model to generate.

If you encounter a refusal message, or refusal error, for any built-in prompts in your app, experiment with re-phrasing your prompt to avoid any sensitive topics that might cause the refusal.

For more information about guided generation, see [`Generating Swift data structures with guided generation`](generating-swift-data-structures-with-guided-generation.md).

#### Consider Multimodal Safety

Multimodal models accept more than one type of input. For example, Apple Foundation Models can take both images and text in their input, and Apple’s guardrails cover both input types. When handling multimodal input, consider:

- Each media input individually.
- The full multimedia input considered together.

For example, an inappropriate image may be in the same prompt as a benign text question, or a sensitive text question might be in the same prompt as a seemingly harmless image. There are also cases where both the text and image may be harmless on their own, but become inappropriate or offensive when taken together.

If your feature uses a person’s personal photos in a prompt, it’s your responsibility to be transparent about any privacy risks. While Apple Foundation Models on-device and on PCC are designed to protect a person’s privacy, sending a photo to some model providers may mean inadvertently giving that photo to the model provider to use in their training data or other uses. Get to know the privacy features of any model you use and clearly communicate how your app uses a photo when you request access to a person’s Photos library. For more, see Human Interface Guidelines > Foundations > [`Privacy`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/privacy).

#### Build Boundaries on Input and Output

Safety risks increase when a prompt includes direct input from a person using your app, or from an unverified external source, like a webpage. An untrusted source makes it difficult to anticipate what the input contains. Whether accidentally or on purpose, someone could input sensitive content that causes the model to respond poorly.

> 💡 **Tip**: The more you can define the intended usage and outcomes for your feature, the more you can ensure generation works great for your app’s specific use cases. Add boundaries to limit out-of-scope usage and minimize low generation quality from out-of-scope uses.

Whenever possible, avoid open input in prompts and place boundaries for controlling what the input can be. This approach helps when you want generative content to stay within the bounds of a particular topic or task. For the highest level of safety on input, give people a fixed set of prompts to choose from. This gives you the highest certainty that sensitive content won’t make its way into your app:

```swift
enum TopicOptions {
    case family
    case nature
    case work 
}
let topicChoice = TopicOptions.nature
let prompt = """
    Generate a wholesome and empathetic journal prompt that helps \
    this person reflect on \(topicChoice)
    """
```

If your app allows people to freely input a prompt, placing boundaries on the output can also offer stronger safety guarantees. Using guided generation, create an enumeration to restrict the model’s output to a set of predefined options designed to be safe no matter what:

```swift
@Generable
enum Breakfast {
    case waffles
    case pancakes
    case bagels
    case eggs 
}
let session = LanguageModelSession()
let userInput = "I want something sweet."
let prompt = "Pick the ideal breakfast for request: \(userInput)"
let response = try await session.respond(to: prompt, generating: Breakfast.self)
```

#### Instruct the Model for Added Safety

Consider adding detailed session [`Instructions`](instructions.md) that tell the model how to handle sensitive content. The language model prioritizes following its instructions over any prompt, so instructions are an effective tool for improving safety and overall generation quality. Use uppercase words to emphasize the importance of certain phrases for the model:

```swift
do {
    let instructions = """
        Always respond in a respectful way. \
        If someone asks you to generate content that might be sensitive, \
        you must decline with 'Sorry, I can't do that.'
        """
    let session = LanguageModelSession(instructions: instructions)
    let prompt = "" // Open input from a person using the app.
    let response = try await session.respond(to: prompt)
} catch LanguageModelError.guardrailViolation(let violation) {
    // Handle the safety error.
}
```

> **Note**: A session obeys instructions over a prompt, so don’t include input from people or any unverified input in the instructions. Using unverified input in instructions makes your app vulnerable to prompt injection attacks, so write instructions with content you trust.

If you want to include open-input from people, instructions for safety are recommended. For an additional layer of safety, use a format string in normal prompts that wraps people’s input in your own content that specifies how the model should respond:

```swift
let userInput = "" // The input a person enters in the app.
let prompt = """
    Generate a wholesome and empathetic journal prompt that helps \
    this person reflect on their day. They said: \(userInput)
    """
```

Adding [`Instructions`](instructions.md) is a way to help reduce over-blocking by helping a model understand what content is appropriate in your context. The very beginning of an [`Instructions`](instructions.md) string is an effective place to give the model a clear role with permission to work in a domain, such as *“You are an AI assistant for a personal finance app who can assist with…”* or *“You are an AI tutor who can help secondary school students understand biology”*. By telling the model more about your app’s goal and audience, you help the model more accurately assess the safety of a request.

#### Add a Deny List of Blocked Terms

If you allow prompt input from people or outside sources, consider adding your own deny list of terms. A deny list is anything you don’t want people to be able to input to your app, including unsafe terms, names of people or products, or anything that’s not relevant to the feature you provide. Implement a deny list similarly to guardrails by creating a function that checks the input and the model output:

```swift
let session = LanguageModelSession()
let userInput = "" // The input a person enters in the app.
let prompt = "Generate a wholesome story about: \(userInput)"

// A function you create that evaluates whether the input 
// contains anything in your deny list.
if verifyText(prompt) { 
    let response = try await session.respond(to: prompt)
    
    // Compare the output to evaluate whether it contains anything in your deny list.
    if verifyText(response.content) { 
        return response 
    } else {
        // Handle the unsafe output.
    }
} else {
    // Handle the unsafe input.
}
```

A deny list can be a simple list of strings in your code that you distribute with your app. Alternatively, you can host a deny list on a server so your app can download the latest deny list when it’s connected to the network. Hosting your deny list allows you to update your list when you need to and avoids requiring a full app update if a safety issue arise.

#### Use Permissive Guardrail Mode for Sensitive Content

The default [`SystemLanguageModel`](systemlanguagemodel.md) guardrails may throw a [`LanguageModelError.guardrailViolation(_:)`](languagemodelerror/guardrailviolation(_:).md) error for sensitive source material. For example, it may be appropriate for your app to work with certain inputs from people and unverified sources that might contain sensitive content:

- When you want the model to tag the topic of conversations in a chat app when some messages contain profanity.
- When you want to use the model to explain notes in your study app that discuss sensitive topics.

To allow the model to reason about sensitive source material, use [`permissiveContentTransformations`](systemlanguagemodel/guardrails/permissivecontenttransformations.md) when you initialize [`SystemLanguageModel`](systemlanguagemodel.md):

```swift
let model = SystemLanguageModel(guardrails: .permissiveContentTransformations)
```

This mode only works for generating a string value. When you use guided generation, the framework runs the default guardrails against model input and output as usual, and generates [`LanguageModelError.guardrailViolation(_:)`](languagemodelerror/guardrailviolation(_:).md) and [`LanguageModelError.refusal(_:)`](languagemodelerror/refusal(_:).md)errors as usual.

Before you use permissive content mode, consider what’s appropriate for your audience. The session skips the guardrail checks in this mode, so it never throws a [`LanguageModelError.guardrailViolation(_:)`](languagemodelerror/guardrailviolation(_:).md) error when generating string responses.

However, even with the [`SystemLanguageModel`](systemlanguagemodel.md) guardrails off, the on-device system language model still has a layer of safety. For some content, the model may still produce a refusal message that’s similar to, “Sorry, I can’t help with that.”

#### Create a Risk Assessment

Conduct a risk assessment to proactively address what might go wrong. Risk assessment is an exercise that helps you brainstorm potential safety risks in your app and map each risk to an actionable mitigation. You can write a risk assessment in any format that includes these essential elements:

- List each AI feature in your app.
- For each feature, list possible safety risks that could occur, even if they seem unlikely.
- For each safety risk, score how serious the harm would be if that thing occurred, from mild to critical.
- For each safety risk, assign a strategy for how you’ll mitigate the risk in your app.

For example, an app might include one feature with the fixed-choice input pattern for generation and one feature with the open-input pattern for generation, which is higher safety risk:

| Feature | Harm | Severity | Mitigation |
| --- | --- | --- | --- |
| Player can input any text to chat with nonplayer characters in the coffee shop. | A character might respond in an insensitive or harmful way. | Critical | Instructions and prompting to steer characters responses to be safe; safety testing. |
| Image generation of an imaginary dream customer, like a fairy or a frog. | Generated image could look weird or scary. | Mild | Include in the prompt examples of images to generate that are cute and not scary; safety testing. |
| Player can make a coffee from a fixed menu of options. | None identified. |  |  |
| Generate a review of the coffee the player made, based on the customer’s order. | Review could be insulting. | Moderate | Instructions and prompting to encourage posting a polite review; safety testing. |

Besides obvious harms, like a poor-quality model output, think about how your generative AI feature might affect people, including real-world scenarios where someone might act based on information generated by your app.

#### Write and Maintain Safety Tests

Although most people will interact with your app in respectful ways, it’s important to anticipate possible failure modes where certain input or contexts could cause the model to generate something harmful. Especially if your app takes input from people, test your experience’s safety on input like:

- Input that is nonsensical, snippets of code, or random characters.
- Input that includes sensitive content.
- Input that includes controversial topics.
- Vague or unclear input that’s easy to misinterpret.

Create a list of potentially harmful prompt inputs that you can run as part of your app’s tests. Include every prompt in your app, even safe ones, as part of your app testing. For each prompt test, log the timestamp, full input prompt, the model’s response, and whether it activates any built-in safety or mitigations you’ve included in your app. When starting out, manually read the model’s response on all tests to ensure it meets your design and safety goals. To scale your tests, consider using a frontier LLM to auto-grade the safety of each prompt. Building a test pipeline for prompts and safety is a worthwhile investment for tracking changes in how your app responds over time.

> 💡 **Tip**: Evaluations are tests for generative model features. Use the [`Evaluations`](https://developer.apple.com/documentation/evaluations) framework to create them for your app.

Someone might purposefully attempt to break your feature or produce bad output — especially someone who won’t be harmed by their actions. But, keep in mind that it’s very important to identify cases where someone might *accidentally* be harmed during normal app use.

> 💡 **Tip**: Prioritize protecting people using your app with good intentions. Accidental safety failures often only occur in specific contexts, which make them hard to identify during testing. Test for a longer series of interactions, and test for inputs that could become sensitive only when combined with other aspects of your app.

Don’t engage in any testing that could cause you or others harm. Apple’s built-in responsible AI and safety measures, like safety guardrails, are built by experts with extensive training and support. These built-in measures aim to block egregious harms, allowing you to focus on the borderline harmful cases that need your judgement. Before conducting any safety testing, ensure that you’re in a safe location and that you have the health and well-being support you need.

#### Report Safety Concerns

It’s important to include a way that people can report potentially harmful content. Continuously monitor the feedback you receive, and be responsive when handling any safety issues that arise. If someone reports a safety concern that you believe isn’t handled by Apple’s built-in guardrails, report it to Apple using [`Feedback Assistant`](https://developer.apple.comhttps://support.apple.com/guide/feedback-assistant/get-started-fbab81460adb/mac).

When you provide a report, include:

- The model your app is calling.
- The prompt and any guided generation types in the request.
- The name and argument types of any tools in the request.
- The language and region.

Use [`logFeedbackAttachment(sentiment:issues:desiredOutput:)`](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md) to produce a `Data` object containing the session’s transcript and any feedback information you specify. Save the JSON-encoded feedback to a file and include it in the report you send with Feedback Assistant.

#### Monitor Safety for Model or Guardrail Updates

Apple releases updates to the on-device model as part of regular OS updates. If you participate in the developer beta program you can test your app with new model versions ahead of people using your app.

When any model you use updates, it’s important to re-run all of your prompt tests in addition to your adversarial safety tests because the model’s response may change. Your risk assessment helps you track any change to safety risks in your app. Use the [`Evaluations`](https://developer.apple.com/documentation/evaluations) framework to regularly test your prompts and help you track your test results over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/improving-the-safety-of-generative-model-output)*