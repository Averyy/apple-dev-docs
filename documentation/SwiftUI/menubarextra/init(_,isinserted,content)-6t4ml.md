# init(_:isInserted:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu bar extra with a key for a localized string to use as the label. The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Parameters

- `titleKey`: The title key to use for the label of the item.
- `isInserted`: Whether the item is inserted in the menu bar. The item may or may not be visible, depending on the number of items present.
- `content`: A `View` to display when the user selects the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(_:isinserted:content:)-6t4ml)*