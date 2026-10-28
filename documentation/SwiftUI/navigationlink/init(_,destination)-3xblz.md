# init(_:destination:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents a destination view, with a text label that the link generates from a localized string key.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(_:destination:)`](./init%28_,destination%29-7d6im.md) instead.

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, destination: Destination)
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
@export(implementation)
nonisolated init<S>(_ title: S, @ContentBuilder destination: () -> Destination) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, destination: Destination) where S : StringProtocol
```

## Parameters

- `titleKey`: A localized string key for creating a text label.
- `destination`: A view for the navigation link to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:destination:)-3xblz)*