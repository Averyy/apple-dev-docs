# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu bar extra with a key for a localized string to use as the label. The extra defines the primary scene of an `App`.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Discussion

When this item is removed from the system menu bar by the user, the application will be automatically quit. As such, it should not be used in conjunction with other scene types in your `App`.

## Parameters

- `titleKey`: The title key to use for the label of the item.
- `content`: A `View` to display when the user selects the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextra/init(_:content:)-4tqs4)*