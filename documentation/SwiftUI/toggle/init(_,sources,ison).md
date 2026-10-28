# init(_:sources:isOn:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle representing a collection of values that generates its label from a localized string resource.

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
@export(implementation)
nonisolated init<C>(_ titleResource: LocalizedStringResource, sources: C, isOn: KeyPath<C.Element, Binding<Bool>>) where C : RandomAccessCollection
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init<C>(_ titleKey: LocalizedStringKey, sources: C, isOn: KeyPath<C.Element, Binding<Bool>>) where C : RandomAccessCollection
```

```swift
nonisolated
init<S, C>(_ title: S, sources: C, isOn: KeyPath<C.Element, Binding<Bool>>) where S : StringProtocol, C : RandomAccessCollection
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See `Text` for more information about localizing strings.

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

- `titleResource`: Text resource for the toggle’s localized title, that describes the purpose of the toggle.
- `sources`: A collection of values used as the source for rendering the Toggle’s state.
- `isOn`: The key path of the values that determines whether the toggle is on, mixed or off.

## See Also

### Creating a toggle for a collection
- [init<C>(sources: C, isOn: KeyPath<C.Element, Binding<Bool>>, label: () -> Label)](./init%28sources,ison,label%29.md)
  Creates a toggle representing a collection of values with a custom label.
- [init(_:image:sources:isOn:)](./init%28_,image,sources,ison%29.md)
  Creates a toggle representing a collection of values that generates its label from a localized string resource and image resource.
- [init(_:systemImage:sources:isOn:)](./init%28_,systemimage,sources,ison%29.md)
  Creates a toggle representing a collection of values that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:sources:ison:))*