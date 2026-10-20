# init(isOn:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
nonisolated
init(isOn: Binding<Bool>, @ContentBuilder label: () -> Label)
```

## Parameters

- `isOn`: A binding to a property that determines whether the toggle is on or off.
- `label`: A view that describes the purpose of the toggle.

## See Also

### Creating a toggle
- [init(_:isOn:)](./init%28_,ison%29.md)
  Creates a toggle that generates its label from a localized string resource.
- [init(_:image:isOn:)](./init%28_,image,ison%29.md)
  Creates a toggle that generates its label from a localized string resource and image resource.
- [init(_:systemImage:isOn:)](./init%28_,systemimage,ison%29.md)
  Creates a toggle that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(ison:label:))*