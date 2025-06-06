# init(isOn:intent:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle performing an `AppIntent`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init<I>(isOn: Bool, intent: I, @ViewBuilder label: () -> Label) where I : AppIntent
```

## Parameters

- `isOn`: Whether the toggle is on or off.
- `intent`: The   to be performed.
- `label`: A view that describes the purpose of the toggle.

## See Also

- [init(_:isOn:intent:)](toggle/init(_:ison:intent:).md)
  Creates a toggle performing an `AppIntent` and generates its label from a localized string key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(ison:intent:label:))*