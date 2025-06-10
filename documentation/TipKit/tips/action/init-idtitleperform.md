# init(id:title:perform:)

**Framework**: TipKit  
**Kind**: init

Creates a tip action that generates its label from a string.

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
nonisolated init(id: String? = nil, title: some StringProtocol, perform handler: @escaping @MainActor () -> Void = {})
```

## Parameters

- `id`: An optional identifier associated with the action. If you don’t specify a value, the system assigns the action’s   to this value.
- `title`: A string that describes the purpose of the tip action.
- `handler`: The function the system calls when the action triggers.

## See Also

- [init(id: String?, perform: () -> Void, () -> Text)](tips/action/init(id:perform:_:).md)
  Creates a tip action that displays a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/action/init(id:title:perform:))*