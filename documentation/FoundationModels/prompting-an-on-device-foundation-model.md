# Prompting an on-device foundation model

**Framework**: Foundation Models

Tailor your prompts to get effective results from an on-device model.

#### Overview

Many prompting techniques are designed for server-based “frontier” foundation models, because they have a larger context window and thinking capabilities. However, when prompting an on-device model, your prompt engineering technique is even more critical because the model you access is much smaller.

To generate accurate, hallucination-free responses, your prompt needs to be concise and specific. To get a better output from the model, some techniques you can use include:

- Use simple, clear instructions
- Iterate and improve your prompt based on the output you receive in testing
- Provide the model with a reasoning field before answering a prompt
- Reduce the thinking the model needs to do
- Split complex prompts into a series of simpler requests
- Add “logic” to conditional prompts with “if-else” statements
- Leverage shot-based prompting — such as one-shot, few-shot, or zero-shot prompts — to provide the model with specific examples of what you need

You’ll need to test your prompts throughout development and evaluate the output to provide a great user experience.

#### Concepts for Creating Great Prompts

With prompt engineering, you structure your requests by refining how you phrase questions, provide context, and format instructions. It also requires testing and iteration of your input to get the results your app needs.

You can also structure prompts to make the model’s response depend on specific conditions or criteria in the input. For example, instead of giving one fixed instruction you can include different conditions, like:

#### Keep Prompts Simple and Clear

Effective prompts use simple language that tells the model what output you want it to provide. The model processes text in units, called , and each model has a maximum number of tokens it can process — the context window size. An on-device model has fewer parameters and a small context window, so it doesn’t have the resources to handle long or confusing prompts. Input to a frontier model might be the length of a full document, but your input to the on-device model needs to be short and succinct. Ask yourself whether your prompt is understandable to a human if they read it quickly, and consider additional strategies to adjust your tone and writing style:

| ✅ Prompting strategies to use | 🚫 Prompting strategies to avoid |
| --- | --- |
| Focus on a single, well-defined goal | Combining multiple unrelated requests |
| Be direct with imperative verbs like “List” or “Create” | Unnecessary politeness or hedging |
| Tell the model what role to play, for example, an interior designer | Passive voice, for example, “code needs to be optimized” |
| Write in direct, conversational tone with simple, clear sentences | Jargon the model might not understand or interpret incorrectly |
| State your request clearly | Too short of a prompt that doesn’t outline the task |
| Limit your prompt to one to three paragraphs | Too long of a prompt that makes it hard to identify what the task is |

An on-device model may get confused with a long and indirect instruction because it contains unnecessary language that doesn’t add value. Instead of indirectly implying what the model needs to do, write a direct command to improve the clarity of the prompt for better results. This clarity also reduces the complexity and context window size for the on-device model.

For more information on managing the context window size, see [`TN3193: Managing the on-device foundation model’s context window`](https://developer.apple.com/documentation/Technotes/tn3193-managing-the-on-device-foundation-model-s-context-window).

#### Give the Model a Role Persona and Tone

By default, the on-device model typically responds to questions in a neutral and respectful tone, with a business-casual persona. Similar to frontier models, you can provide a role or persona to dramatically change how the on-device model responds to your prompt.

A  is the functional position or job that you instruct the model to assume, while a  reflects the personality of the model. You often use both in prompts; for example:

Here the role is “a senior software engineer,” and the persona is “mentoring junior developers.”

The model phrases its response differently to match a persona, for example, “mentoring junior developers” or “evaluating developer coding” even when you give it the same input for the same task.

To give the model a role, use the phrase “you are”:

Use the phrase “expert” to get the model to speak with more authority and detail on a topic.

Similarly, change the model’s behavior by providing a role or persona for the person using your app. By default, the on-device model thinks it’s talking to a person, so tell the model more about who  person is:

The student persona causes the model to respond as if speaking to a child in the first grade, while the ghost persona causes the model to respond as if speaking to a ghost in an alchemy shop.

Change the model’s tone by writing your prompt in a voice you want the model to match. For example, if you write your prompt in a peppy and cheerful way, or talk like a cowboy, the model responds with a matching tone.

#### Iterate and Improve Instruction Following

 refers to a foundation model’s ability to carry out a request exactly as written in your [`Prompt`](prompt.md) and [`Instructions`](instructions.md). Prompt engineering involves iteration to test and refine input — based on the results you get — to improve accuracy and consistency. If you notice the model isn’t following instructions as well as you need, consider the following strategies:

| Strategy | Approach |
| --- | --- |
| Improve clarity | Improve the wording of your input to make it more direct, concise, and easier to read. |
| Use emphasis | Emphasize the importance of a command by adding words like “must, “should”, “do not” or avoid”. |
| Repeat yourself | Try repeating key instructions at the end of your input to emphasize the importance. |

Instead of trying to enforce accuracy, use a succinct prompt like “Answer this question” and evaluate the results you get.

After you try any strategy, take the time to evaluate it to see if the result gets closer to what you need. If the model can’t follow your prompt, it might be unreliable in some use cases. Try cutting back the number of times you repeat a phrase, or the number of words you emphasize, to make your prompt more effective. Unreliable prompts break easily when conditions change slightly.

Another prompting strategy is to split your request into a series of simpler requests. This is particularly useful after trying different strategies that don’t improve the quality of the results.

#### Reduce How Much Thinking the Model Needs to Do

A model’s reasoning ability is how well it thinks through a problem like a human, handles logical puzzles, or creates a logical plan to handle a request. Because of their smaller size, on-device models have limited reasoning abilities. You may be able to help an on-device model  a challenging task by providing additional support for its reasoning.

For complex tasks, simple language prompts might not have enough detail about how the model can accomplish a task. Instead, reduce the reasoning burden on the model by giving it a step-by-step plan. This approach tells the model more precisely how to do the task:

If you find the model isn’t accomplishing the task reliably, break up the steps across multiple [`LanguageModelSession`](languagemodelsession.md) instances to focus on one part at a time with a new context window. Typically, it’s a best practice to start with a single request because multiple requests can result in longer inference time. But, if the result doesn’t meet your expectations, try splitting steps into multiple requests.

#### Turn Conditional Prompting Into Programming Logic

 prompting is where you embed if-else logic into your prompt. A server-based frontier model has the context window and reasoning abilities to handle a lengthy list of instructions for how to handle different requests. An on-device model can handle some conditionals or light reasoning, like:

But, too much conditional complexity can affect the on-device model’s ability to follow instructions.

When the on-device model output doesn’t meet your expectations, try customizing your conditional prompt to the current context. For example, the following conditional prompt contains several sentences that break up what the model needs to do:

```swift
let instructions = """
    You are a friendly innkeeper. Generate a greeting to a new guest that walks in the door.
    IF the guest is a sorcerer, comment on their magical appearance.
    IF the guest is a bard, ask if they're willing to play music for the inn tonight.
    IF the guest is a soldier, ask if there’s been any dangerous activity in the area.
    There is one single and one double room available.
    """
```

Instead, use programming logic to customize the prompt based on known information:

```swift
var customGreeting = ""
switch role {
case .bard:
    customGreeting = """
        This guest is a bard. Ask if they’re willing to play music for the inn tonight.
        """
case .soldier:
    customGreeting = """
        This guest is a soldier. Ask if there’s been any dangerous activity in the area.
        """
case .sorcerer:
    customGreeting = """
        This guest is a sorcerer. Comment on their magical appearance.
        """
default:
    customGreeting = "This guest is a weary traveler."
}

let instructions = """
    You are a friendly inn keeper. Generate a greeting to a new guest that walks in the door.
    \(customGreeting)
    There is one single and one double room available.
    """
```

When you customize instructions programmatically, the model doesn’t get distracted or confused by conditionals that don’t apply in the situation. This approach also reduces the context window size.

#### Provide Simple Input Output Examples

 prompting is when you provide the on-device model with a few examples of the output you want. For example, the following shows the model different kinds of coffee shop customers it needs to generate:

```swift
// Instructions that contain JSON key-value pairs that represent the structure
// of a customer. The structure tells the model that each customer must have
// a `name`, `imageDescription`, and `coffeeOrder` fields.
let instructions = """
    Create an NPC customer with a fun personality suitable for the dream realm. \
    Have the customer order coffee. Here are some examples to inspire you:

    {name: "Thimblefoot", imageDescription: "A horse with a rainbow mane", \
    coffeeOrder: "I would like a coffee that's refreshing and sweet, like the grass in a summer meadow."}
    {name: "Spiderkid", imageDescription: "A furry spider with a cool baseball cap", \
    coffeeOrder: "An iced coffee please, that's as spooky as I am!"}
    {name: "Wise Fairy", imageDescription: "A blue, glowing fairy that radiates wisdom and sparkles", \
    coffeeOrder: "Something simple and plant-based, please. A beverage that restores my wise energy."}
    """
```

Few-shot prompting also works with , which formats the model’s output by using a custom type you define. In the previous prompt, each example might correspond to a [`Generable`](generable.md) structure you create named `NPC`:

```swift
@Generable
struct NPC: Equatable {
    let name: String
    let coffeeOrder: String
    let imageDescription: String
}
```

On-device models need simpler examples for few-shot prompts than what you can use with server-based frontier models. Try giving the model between 2-15 examples, and keep each example as simple as possible. If you provide a long or complex example, the on-device model may start to repeat your example or hallucinate details of your example in its response.

For more information on guided generation, see [`Generating Swift data structures with guided generation`](generating-swift-data-structures-with-guided-generation.md).

#### Handle on Device Reasoning

Reasoning prompt techniques, like “think through this problem step by step”, can result in unexpected text being inserted into your [`Generable`](generable.md) structure if the model doesn’t have a place for its reasoning. To keep reasoning explanations out of your structure, try giving the model a specific field where it can put its reasoning. Make sure the reasoning field is the first property so the model can provide reasoning details before answering the prompt:

```swift
@Generable
struct ReasonableAnswer {
    // A property the model uses for reasoning.
    var reasoningSteps: String
    
    @Guide(description: "The answer only.")
    var answer: MyCustomGenerableType // Replace with your custom generable type.
}
```

Using your custom [`Generable`](generable.md) type, prompt the model:

```swift
let instructions = """
    Answer the person's question.
    1. Begin your response with a plan to solve this question.
    2. Follow your plan's steps and show your work.
    3. Deliver the final answer in `answer`.
    """
var session = LanguageModelSession(instructions: instructions)

// The answer should be 30 days.
let prompt = "How many days are in the month of September?"
let response = try await session.respond(
    to: prompt,
    generating: ReasonableAnswer.self
)
```

You may see the model fail to reason its way to a correct answer, or it may answer unreliably — occasionally answering correctly, and sometimes not. If this happens, the tasks in your prompt may be too difficult for the on-device model to process, regardless of how you structure the prompt.

#### Provide Actionable Feedback

When you encounter something with the on-device model that you expect to work but it doesn’t, file a report that includes your prompt with Feedback Assistant to help improve the system model. To submit feedback about model behavior through Feedback Assistant, see [`logFeedbackAttachment(sentiment:issues:desiredOutput:)`](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md).

## See Also

- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)
  Optimize token consumption and improve response times by profiling your app’s model usage with Instruments.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/prompting-an-on-device-foundation-model)*