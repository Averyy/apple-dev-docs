# init(_:image:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu bar extra with a named image to use as the items label. The provided title will be used by the accessibility system.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: String, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Label<Text, Image>` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, @ContentBuilder content: () -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image: String, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, image: ImageResource, @ContentBuilder content: () -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, image: String, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Discussion

The item defines the primary scene of an `App`.

When this item is removed from the system menu bar by the user, the application will be automatically quit. As such, it should not be used in conjunction with other scene types in your `App`.

## Parameters

- `titleKey`: The localized string key to use for the accessibility label of the item.
- `image`: The name of an image in the app’s bundle to use as the label.
- `content`: A `View` to display when the user selects the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(_:image:content:)-1n53m)*