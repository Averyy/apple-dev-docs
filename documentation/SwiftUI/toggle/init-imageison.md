# init(_:image:isOn:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle that generates its label from a localized string resource and image resource.

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
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, isOn: Binding<Bool>)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the toggle’s localized title, that describes the purpose of the toggle.
- `image`: The name of the image resource to lookup.
- `isOn`: A binding to a property that indicates whether the toggle is on or off.

## See Also

- [init(_:isOn:)](toggle/init(_:ison:).md)
  Creates a toggle that generates its label from a localized string resource.
- [init(isOn: Binding<Bool>, label: () -> Label)](toggle/init(ison:label:).md)
  Creates a toggle that displays a custom label.
- [init(_:systemImage:isOn:)](toggle/init(_:systemimage:ison:).md)
  Creates a toggle that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:image:ison:))*