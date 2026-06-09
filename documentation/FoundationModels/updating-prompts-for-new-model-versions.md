# Updating prompts for new model versions

**Framework**: Foundation Models

Manage the prompts your app uses by versioning them to make the most out of model improvements.

#### Overview

When a new version of the foundation model your app uses becomes available, test the prompts your app uses against the old and new model versions to check whether there are unexpected differences in output. The new version of a model brings with it improvements, like improved tool calling and the model’s ability to follow instructions.

To adopt the latest model improvements, and make sure your app works for people on all model versions:

- Monitor when Apple releases a new model version by visiting [`Foundation Models updates`](https://developer.apple.com/documentation/Updates/FoundationModels).
- Record what output your prompt produces for the previous model version.
- Compare the previous model output against the new model to determine whether you need to update the prompt.
- If an update is necessary, version your prompts for each model your app supports.

For more information on prompting an on-device model, see [`Prompting an on-device foundation model`](prompting-an-on-device-foundation-model.md).

#### Use Availability Checks to Version Your Prompts

Ideally, your prompt should be relatively stable across model versions. However, to take advantage of new model improvements, or handle behavioral changes, choose a strategy of prompt versioning that works best for your app.

The strategy you deploy influences how easily you can update your prompt when you need. There are several common strategies for prompt versioning that offer varying levels of simplicity versus control. For example, hard coded prompts are difficult to update because you need to wait for a new release of your app, whereas a server-based solution provides the most flexibility.

When you want to load a different version of your prompt, use the availability attribute to check for the system version:

```swift
if #available(iOS 26.4, macOS 26.4, visionOS 26.4, *) {
    // Use the prompt that you update for the the latest system version.
} else {
    // Use the prompt for the model in 26.0 to 26.3.
}
```

Order the availability attribute from the newest version to the oldest version. The asterisk (`*`) indicates availability to future versions newer than the OS version you list. The availability of the [`Foundation Models`](FoundationModels.md) framework starts at 26.0, so you don’t need to check for versions prior to that.

#### Record the Output Your Prompt Produced Before Updating

Because the older model is only included as part of the beta program, it’s essential to produce a record of what output your prompt produces with the prior model. The method you use to track model input and output responses is up to you. The goal is so you can identify how the model responds to your prompt when the model changes.

One way to maintain your prompts is to put them in individual text files instead of hardcoding them. This way, you create a library of prompts that you can organize by feature and include additional details about the prompt. For example, you might use JSON or YAML to describe more details that you want to associate with the prompt. With a clear naming structure, a single text file can identify what the prompt does and include the version of the prompt. For example, a prompt you associate with a customer support feature that summarizes a ticket might have the name and the version of the prompt, like `support-ticket-summarizer-v1.0`. If you need to update the prompt for a new model version, create a new text file that contains the necessary modifications.

Each time you modify your prompt it can also be helpful to keep a changelog you associate with it to know what changes.

#### Use Xcode String Catalogs to Version Your Prompts

Xcode string catalogs let you localize and translate all your app’s text in a visual editor. You don’t need to localize your prompts for all of the languages you support, but doing so can help the model respond more reliably in the correct language. For more information on localization, see [`Supporting languages and locales with Foundation Models`](supporting-languages-and-locales-with-foundation-models.md).

In addition to localization, you can use string catalogs to manage your prompts in one convenient location. To create a new string catalog for your prompts:

1. In Xcode, choose File > New > File from Template.
2. In the Template Selection window, select String Catalog, then click Next.
3. Enter a name for the catalog, like “Prompts,” and click Create.

The string catalog allows you to add a new key, like `support-ticket-summarizer-v1.0` that you use to get the prompt you associate with it. The following image shows a string catalog with two English prompts and one in Spanish:

![A screenshot that shows a string catalog with two default prompts. One prompt](https://docs-assets.developer.apple.com/published/26a5b1cff0347e187cae6c949c6bef17/updating-prompts-for-new-model-versions-string-catalog%402x.png)

Access the prompt in your app by initializing a `String` with the the unique key in the string catalog you specify:

```swift
if #available(iOS 26.4, macOS 26.4, visionOS 26.4, *) {
    return String(localized: "support-ticket-summarizer-v1.1", table: "Prompts")
} else {
    return String(localized: "support-ticket-summarizer-v1.0", table: "Prompts")
}
```

For more information about Xcode string catalogs, see [`Localizing and varying text with a string catalog`](https://developer.apple.com/documentation/Xcode/localizing-and-varying-text-with-a-string-catalog).

#### Use a Server to Version Your Prompts

Using a server for prompt versioning lets your app fetch prompts dynamically at runtime, enabling much faster updates when you need them. This allows you to test new iterations across a small subset of people or even perform rollbacks if something is wrong with a prompt.

How you implement a server-based solution is up to you, but consider a common configuration check when your app launches. On app launch, perform a check with your server to get the latest prompt configuration and cache the results locally. Doing so makes sure the latest updates are available when you want to prompt the on-device foundation model offline.

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Managing the context window](managing-the-context-window.md)
  Optimize your app’s token usage when prompting a model with the Foundation Models framework.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.
- [struct TranscriptErrorHandlingPolicy](transcripterrorhandlingpolicy.md)
  Options for controlling how a language model session manages the transcript when errors occur.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.
- [struct ContextOptions](contextoptions.md)
  Options that configure details that should appear in the prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/updating-prompts-for-new-model-versions)*