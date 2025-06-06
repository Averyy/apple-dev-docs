# requestConfirmation(for:dialog:view:)

**Framework**: App Intents  
**Kind**: method

Use `requestConfirmation` when you need to the ask user to confirm the parameter value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
final func requestConfirmation<ViewType>(for itemToConfirm: Value.ValueType, dialog: IntentDialog? = nil, @ViewBuilder view: () -> ViewType) async throws -> Bool where ViewType : View
```

## Parameters

- `itemToConfirm`: The items to be presented to the user for confirmation
- `dialog`: A custom dialog that may be used when prompting the user for the value
- `view`: A view to display when requesting confirmation.

## See Also

- [func requestConfirmation(for: Value.ValueType, dialog: IntentDialog?) async throws -> Bool](intentparameter/requestconfirmation(for:dialog:).md)
  Request that the user confirm the parameter value.
- [func requestConfirmation<ViewType>(for: Value.ValueType, dialog: IntentDialog?, view: ViewType) async throws -> Bool](intentparameter/requestconfirmation(for:dialog:view:)-6hiyi.md)
  Use `requestConfirmation` when you need to the ask user to confirm the parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/requestconfirmation(for:dialog:view:)-9z0pe)*