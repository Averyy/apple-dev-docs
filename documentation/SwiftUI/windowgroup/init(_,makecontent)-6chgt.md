# init(_:makeContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a window group with a localized title.

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
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder makeContent: @escaping () -> Content)
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
nonisolated init<S>(_ title: S, @ContentBuilder makeContent: @escaping () -> Content) where S : StringProtocol
```

## Discussion

The window group uses the specified content as a template to create each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

## Parameters

- `titleResource`: The title resource to use for the group’s title.
- `makeContent`: A closure that creates the content for each instance of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(_:makecontent:)-6chgt)*