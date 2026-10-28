# init(_:destination:isActive:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents a destination view when active, with a text label that the link generates from a title string.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS 13.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 9.0

> **Deprecated**: Use [`init(_:value:)`](./init%28_,value%29-9ziux.md) instead. For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
nonisolated
init<S>(_ title: S, destination: Destination, isActive: Binding<Bool>) where S : StringProtocol
```

Available when `Label` is `Text` and `Destination` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)
```

## Parameters

- `title`: A string for creating a text label.
- `destination`: A view for the navigation link to present.
- `isActive`: A binding to a Boolean value that indicates whether `destination` is currently presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(_:destination:isactive:)-3v44)*