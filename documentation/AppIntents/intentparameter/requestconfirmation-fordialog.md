# requestConfirmation(for:dialog:)

**Framework**: App Intents  
**Kind**: method

Request that the user confirm the parameter value.

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
final func requestConfirmation(for itemToConfirm: Value.ValueType, dialog: IntentDialog? = nil) async throws -> Bool
```

#### Return Value

Whether or not the user confirmed the value

## Parameters

- `itemToConfirm`: The items to be presented to the user for confirmation
- `dialog`: A custom dialog that may be used when prompting the user for the value

## See Also

- [func requestConfirmation<ViewType>(for: Value.ValueType, dialog: IntentDialog?, view: ViewType) async throws -> Bool](intentparameter/requestconfirmation(for:dialog:view:)-6hiyi.md)
  Use `requestConfirmation` when you need to the ask user to confirm the parameter value.
- [func requestConfirmation<ViewType>(for: Value.ValueType, dialog: IntentDialog?, view: () -> ViewType) async throws -> Bool](intentparameter/requestconfirmation(for:dialog:view:)-9z0pe.md)
  Use `requestConfirmation` when you need to the ask user to confirm the parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/requestconfirmation(for:dialog:))*