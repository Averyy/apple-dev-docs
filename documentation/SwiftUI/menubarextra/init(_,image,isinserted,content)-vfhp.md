# init(_:image:isInserted:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu bar extra with a named image to use as the items label. The provided title will be used by the accessibility system.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image: String, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Label<Text, Image>` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: String, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, image: ImageResource, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, image: String, isInserted: Binding<Bool>, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Discussion

The item will be displayed in the system menu bar when the specified binding is set to `true`. If the user removes the item from the menu bar, the binding will be set to `false`.

## Parameters

- `titleResource`: The localized string resource to use for the accessibility label of the item.
- `image`: The name of an image in the app’s bundle to use as the label.
- `isInserted`: Whether the item is inserted in the menu bar. The item may or may not be visible, depending on the number of items present.
- `content`: A `View` to display when the user selects the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(_:image:isinserted:content:)-vfhp)*