# init(_:sources:isOn:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle representing a collection of values that generates its label from a localized string key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<C>(_ titleKey: LocalizedStringKey, sources: C, isOn: KeyPath<C.Element, Binding<Bool>>) where C : RandomAccessCollection
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
- `sources`: A collection of values used as the source for rendering the   Toggle’s state.
- `isOn`: The key path of the values that determines whether the toggle   is on, mixed or off.

## See Also

- [init<C>(sources: C, isOn: KeyPath<C.Element, Binding<Bool>>, label: () -> Label)](toggle/init(sources:ison:label:).md)
  Creates a toggle representing a collection of values with a custom label.
- [init(_:image:sources:isOn:)](toggle/init(_:image:sources:ison:).md)
  Creates a toggle representing a collection of values that generates its label from a localized string key and image resource.
- [init(_:systemImage:sources:isOn:)](toggle/init(_:systemimage:sources:ison:).md)
  Creates a toggle representing a collection of values that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:sources:ison:))*