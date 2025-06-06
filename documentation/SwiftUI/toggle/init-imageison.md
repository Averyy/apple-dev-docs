# init(_:image:isOn:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle that generates its label from a localized string key and image resource.

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
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, isOn: Binding<Bool>)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See `Text` for more information about localizing strings.

## Parameters

- `titleKey`: The key for the toggle’s localized title, that describes   the purpose of the toggle.
- `image`: The name of the image resource to lookup.
- `isOn`: A binding to a property that indicates whether the toggle is   on or off.

## See Also

- [init(_:isOn:)](toggle/init(_:ison:).md)
  Creates a toggle that generates its label from a localized string key.
- [init(isOn: Binding<Bool>, label: () -> Label)](toggle/init(ison:label:).md)
  Creates a toggle that displays a custom label.
- [init(_:systemImage:isOn:)](toggle/init(_:systemimage:ison:).md)
  Creates a toggle that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:image:ison:))*