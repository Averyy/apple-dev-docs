# init(isOn:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle that displays a custom label.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(isOn: Binding<Bool>, @ViewBuilder label: () -> Label)
```

## Parameters

- `isOn`: A binding to a property that determines whether the toggle is on   or off.
- `label`: A view that describes the purpose of the toggle.

## See Also

- [init(_:isOn:)](toggle/init(_:ison:).md)
  Creates a toggle that generates its label from a localized string key.
- [init(_:image:isOn:)](toggle/init(_:image:ison:).md)
  Creates a toggle that generates its label from a localized string key and image resource.
- [init(_:systemImage:isOn:)](toggle/init(_:systemimage:ison:).md)
  Creates a toggle that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(ison:label:))*