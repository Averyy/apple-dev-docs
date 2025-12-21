# requestChoice(between:dialog:)

**Framework**: App Intents  
**Kind**: method

Pauses the app intent to request a person to choose from several options.

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
func requestChoice(between options: [IntentChoiceOption], dialog: IntentDialog? = nil) async throws -> IntentChoiceOption
```

#### Return Value

The value that represents the person’s selection.

#### Discussion

Call this method in your app intent’s [`perform()`](appintent/perform().md) method when you need a person to confirm an action, disambiguate between possibilities, or select a specific variation of the intent’s behavior before proceeding.

The system presents a standard interface — for example, a modal sheet or alert — using the provided `dialog`, the `content` view for context, and buttons for each [`IntentChoiceOption`](intentchoiceoption.md). The app intent’s execution resumes only after the person selects an option.

> **Note**: An error if the person explicitly cancels the app intent; for example, if they use a system-provided cancel button or gesture, or by selecting an option you create using [`cancel`](intentchoiceoption/cancel.md).

## Parameters

- `options`: An array of options to choose from.   The order of options in this array determines the order of options in the UI, excluding the option to cancel the   choice. The system automatically handles the placement of the cancel option according to platform conventions.
- `dialog`: Instructional text or a question to help the person to choose an option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestchoice(between:dialog:))*