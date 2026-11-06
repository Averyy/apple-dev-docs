# ToolbarContainerBehavior

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Whether a container acts as a toolbar container, reading the toolbar content of its child views and placing that content into its own bar.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
struct ToolbarContainerBehavior
```

## Overview

For example, if your app has a split view where the detail column has multiple child `NavigationStack`s, set the `toolbarContainerBehavior` to `.local` on each stack so that each one renders its own toolbar, instead of their toolbar content being rendered in a single toolbar managed by the split view.

## Topics

### Type Properties
- [static let automatic: ToolbarContainerBehavior](./toolbarcontainerbehavior/automatic.md)
  The system decides whether this container renders the toolbar, or whether its toolbar content integrates into a parent container’s bar.
- [static let local: ToolbarContainerBehavior](./toolbarcontainerbehavior/local.md)
  This container reads the toolbar content of its child views and always renders the content as a distinct bar in this container.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontainerbehavior)*