# init(_:id:makeContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a window group with a localized title string and an identifier.

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
nonisolated init(_ titleResource: LocalizedStringResource, id: String, @ContentBuilder makeContent: @escaping () -> Content)
```

Available when `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ title: Text, id: String, @ContentBuilder makeContent: @escaping () -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, id: String, @ContentBuilder makeContent: @escaping () -> Content)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, id: String, @ContentBuilder makeContent: @escaping () -> Content) where S : StringProtocol
```

## Discussion

The window group uses the specified content as a template to create each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

## Parameters

- `titleResource`: The title resource to use for the title of the group.
- `id`: A string that uniquely identifies the window group. Identifiers must be unique among the window groups in your app.
- `makeContent`: A closure that creates the content for each instance of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(_:id:makecontent:)-1oaw9)*