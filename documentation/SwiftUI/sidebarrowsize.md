# SidebarRowSize

**Framework**: SwiftUI  
**Kind**: enum

The standard sizes of sidebar rows.

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
enum SidebarRowSize
```

#### Overview

On macOS, sidebar rows have three different sizes: small, medium, and large. The size is primarily controlled by the current users’ “Sidebar Icon Size” in Appearance settings, and applies to all applications.

On all other platforms, the only supported sidebar size is `.medium`.

This size can be read or written in the environment using `EnvironmentValues.sidebarRowSize`.

## Topics

### Getting row sizes
- [SidebarRowSize.small](sidebarrowsize/small.md)
  The standard “small” row size
- [SidebarRowSize.medium](sidebarrowsize/medium.md)
  The standard “medium” row size
- [SidebarRowSize.large](sidebarrowsize/large.md)
  The standard “large” row size

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var sidebarRowSize: SidebarRowSize](environmentvalues/sidebarrowsize.md)
  The current size of sidebar rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sidebarrowsize)*