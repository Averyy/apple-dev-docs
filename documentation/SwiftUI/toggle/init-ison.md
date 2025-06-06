# init(_:isOn:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle that generates its label from a localized string key.

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
init(_ titleKey: LocalizedStringKey, isOn: Binding<Bool>)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See `Text` for more information about localizing strings.

## Parameters

- `titleKey`: The key for the toggle’s localized title, that describes   the purpose of the toggle.
- `isOn`: A binding to a property that indicates whether the toggle is   on or off.

## See Also

- [init(isOn: Binding<Bool>, label: () -> Label)](toggle/init(ison:label:).md)
  Creates a toggle that displays a custom label.
- [init(_:image:isOn:)](toggle/init(_:image:ison:).md)
  Creates a toggle that generates its label from a localized string key and image resource.
- [init(_:systemImage:isOn:)](toggle/init(_:systemimage:ison:).md)
  Creates a toggle that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:ison:))*