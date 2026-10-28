# init(_:destination:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents a destination view, with a text label that the link generates from a title string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@export(implementation)
nonisolated init<S>(_ title: S, @ContentBuilder destination: () -> Destination) where S : StringProtocol
```

Available when `Label` is `Text` and `Destination` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, @ContentBuilder destination: () -> Destination)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder destination: () -> Destination)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, destination: Destination)
```

```swift
nonisolated
init<S>(_ title: S, destination: Destination) where S : StringProtocol
```

## Parameters

- `title`: A string for creating a text label.
- `destination`: A view for the navigation link to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:destination:)-6z03e)*