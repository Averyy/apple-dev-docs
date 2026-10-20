# requestConfirmation(for:dialog:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

Request that the user confirm the parameter value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
final func requestConfirmation(for itemToConfirm: Value.ValueType, dialog: IntentDialog? = nil) async throws -> Bool
```

Available when `Value` conforms to `_IntentValue` and `Sendable`.

#### Return Value

Whether or not the user confirmed the value

## Parameters

- `itemToConfirm`: The items to be presented to the user for confirmation
- `dialog`: A custom dialog that may be used when prompting the user for the value

## See Also

### Requesting confirmation
- [func requestConfirmation<ViewType>(for: Value.ValueType, dialog: IntentDialog?, view: ViewType) async throws -> Bool](./requestconfirmation%28for,dialog,view%29-6hiyi.md)
  Use `requestConfirmation` when you need to the ask user to confirm the parameter value.
- [func requestConfirmation<ViewType>(for: Value.ValueType, dialog: IntentDialog?, view: () -> ViewType) async throws -> Bool](./requestconfirmation%28for,dialog,view%29-9z0pe.md)
  Use `requestConfirmation` when you need to the ask user to confirm the parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/requestconfirmation(for:dialog:))*