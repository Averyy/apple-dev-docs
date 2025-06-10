# init(id:perform:_:)

**Framework**: TipKit  
**Kind**: init

Creates a tip action that displays a custom label.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@preconcurrency
init(id: String? = nil, perform handler: @escaping @MainActor () -> Void = {}, _ label: @escaping () -> Text)
```

## Parameters

- `id`: An optional identifier associated with the action. If you don’t specify a value, the system assigns the action’s   to this value.
- `handler`: The function the system calls when the action triggers.
- `label`: A view that describes the purpose of the tip action.

## See Also

- [init(id: String?, title: some StringProtocol, perform: () -> Void)](tips/action/init(id:title:perform:).md)
  Creates a tip action that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/action/init(id:perform:_:))*