# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu that generates its label from a string.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content) where Label == Text, S : StringProtocol
```

Available when `Label` conforms to `View` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content) where Label == Text
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content) where Label == Text
```

## Parameters

- `title`: A string that describes the contents of the menu.
- `content`: A group of menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:content:)-7tkrw)*