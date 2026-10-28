# init(_:makeContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a window group with a title string.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@export(implementation)
nonisolated init<S>(_ title: S, @ContentBuilder makeContent: @escaping () -> Content) where S : StringProtocol
```

Available when `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ title: Text, @ContentBuilder makeContent: @escaping () -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, @ContentBuilder makeContent: @escaping () -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder makeContent: @escaping () -> Content)
```

## Discussion

The window group uses the specified content as a template to create each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

## Parameters

- `title`: The string to use for the title of the group.
- `makeContent`: A closure that creates the content for each instance of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(_:makecontent:)-98g70)*