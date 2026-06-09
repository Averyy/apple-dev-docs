# requestChoice(between:dialog:content:)

**Framework**: App Intents  
**Kind**: method

Pauses the app intent, asks the person to choose from the specified options, and provides additional content related to those options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func requestChoice<Content>(between options: [IntentChoiceOption], dialog: IntentDialog? = nil, @ViewBuilder content: () -> Content) async throws -> IntentChoiceOption where Content : View
```

#### Return Value

The option the person chose.

#### Discussion

> **Note**: An error if the person chooses a cancel option from the interface.

Call this method from the [`perform()`](appintent/perform().md) method of your app intent when you need someone to confirm an action, disambiguate from a set of possibilities, or select an intent-specific behavior before proceeding. The system displays a standard interface with the provided set of options and asks the person to choose one. When someone makes a selection, the method returns the option and your app intent continues to run. This method throws an error if someone cancels the request using a cancel button, a [`cancel`](intentchoiceoption/cancel.md) option, or a system-provided gesture.

## Parameters

- `options`: The options to choose from. The prompt displays the options in the same order they appear in the array, with one exception. If the list includes the [`cancel`](intentchoiceoption/cancel.md) option, the system places that option according to the platform’s conventions.
- `dialog`: The localized text you want the system to display or speak. Provide instructional text or a question to help the person choose an option.
- `content`: A closure that returns the view to display with the prompt. Use this closure to return a view with information to help someone make a decision.

## See Also

- [func requestChoice(between: [IntentChoiceOption], dialog: IntentDialog?) async throws -> IntentChoiceOption](appintent/requestchoice(between:dialog:).md)
  Pauses the app intent and asks the person to choose an option from the specified list.
- [func requestChoice<Content>(between: [IntentChoiceOption], dialog: IntentDialog?, view: Content) async throws -> IntentChoiceOption](appintent/requestchoice(between:dialog:view:).md)
  Pauses the app intent, asks the person to choose from the specified options, and provides a view with additional data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestchoice(between:dialog:content:))*