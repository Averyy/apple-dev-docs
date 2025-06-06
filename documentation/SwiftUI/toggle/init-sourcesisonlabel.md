# init(sources:isOn:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle representing a collection of values with a custom label.

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
init<C>(sources: C, isOn: KeyPath<C.Element, Binding<Bool>>, @ViewBuilder label: () -> Label) where C : RandomAccessCollection
```

#### Discussion

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

Toggle(sources: $alarms, isOn: \.isOn) {
    Text("Enable all alarms")
}
```

## Parameters

- `sources`: A collection of values used as the source for rendering the   Toggle’s state.
- `isOn`: The key path of the values that determines whether the toggle   is on, mixed or off.
- `label`: A view that describes the purpose of the toggle.

## See Also

- [init(_:sources:isOn:)](toggle/init(_:sources:ison:).md)
  Creates a toggle representing a collection of values that generates its label from a localized string key.
- [init(_:image:sources:isOn:)](toggle/init(_:image:sources:ison:).md)
  Creates a toggle representing a collection of values that generates its label from a localized string key and image resource.
- [init(_:systemImage:sources:isOn:)](toggle/init(_:systemimage:sources:ison:).md)
  Creates a toggle representing a collection of values that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(sources:ison:label:))*