# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a window group with a title string.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0 (renamed: init(_:makeContent:))
- iPadOS 14.0+ - Deprecated in 18.0 (renamed: init(_:makeContent:))
- Mac Catalyst 14.0+ - Deprecated in 18.0 (renamed: init(_:makeContent:))
- macOS 11.0+ - Deprecated in 15.0 (renamed: init(_:makeContent:))
- tvOS 14.0+ - Deprecated in 18.0 (renamed: init(_:makeContent:))
- visionOS 1.0+ - Deprecated in 2.0 (renamed: init(_:makeContent:))
- watchOS 7.0+ - Deprecated in 11.0 (renamed: init(_:makeContent:))

> **Deprecated**: Use the initializer which takes an escaping content builder instead.

## Declaration

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

**Other overloads**:

```swift
nonisolated
init(_ title: Text, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

## Discussion

The window group uses the specified content as a template to create each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

## Parameters

- `title`: The string to use for the title of the group.
- `content`: A closure that creates the content for each instance of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(_:content:)-82t24)*