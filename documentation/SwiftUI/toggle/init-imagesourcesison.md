# init(_:image:sources:isOn:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle representing a collection of values that generates its label from a localized string key and image resource.

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
init<C>(_ titleKey: LocalizedStringKey, image: ImageResource, sources: C, isOn: KeyPath<C.Element, Binding<Bool>>) where C : RandomAccessCollection
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See `Text` for more information about localizing strings.

The following example creates a single toggle that represents the state of multiple alarms:

```swift
struct Alarm: Hashable, Identifiable {
    var id = UUID()
    var isOn = false
    var name = ""
}

@State private var alarms = [
    Alarm(isOn: true, name: "Morning"),
    Alarm(isOn: false, name: "Evening")
]

Toggle("Enable all alarms", sources: $alarms, isOn: \.isOn)
```

## Parameters

- `titleKey`: The key for the toggle’s localized title, that describes   the purpose of the toggle.
- `image`: The name of the image resource to lookup.
- `sources`: A collection of values used as the source for rendering the   Toggle’s state.
- `isOn`: The key path of the values that determines whether the toggle   is on, mixed or off.

## See Also

- [init(_:sources:isOn:)](toggle/init(_:sources:ison:).md)
  Creates a toggle representing a collection of values that generates its label from a localized string key.
- [init<C>(sources: C, isOn: KeyPath<C.Element, Binding<Bool>>, label: () -> Label)](toggle/init(sources:ison:label:).md)
  Creates a toggle representing a collection of values with a custom label.
- [init(_:systemImage:sources:isOn:)](toggle/init(_:systemimage:sources:ison:).md)
  Creates a toggle representing a collection of values that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:image:sources:ison:))*