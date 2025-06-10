# requestConfirmation(for:dialog:)

**Framework**: App Intents  
**Kind**: method

Use `requestConfirmation` when you need to the ask user to confirm the parameter value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func requestConfirmation(for itemToConfirm: Value.ValueType, dialog: IntentDialog? = nil) async throws -> Bool
```

#### Return Value

Whether or not the user confirmed the value

## Parameters

- `itemToConfirm`: The items to be presented to the user for confirmation
- `dialog`: A custom dialog that may be used when prompting the user for the value


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametercontext/requestconfirmation(for:dialog:))*