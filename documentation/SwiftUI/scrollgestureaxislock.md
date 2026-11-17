# ScrollGestureAxisLock

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Controls whether a scrollable view locks scroll gestures to one axis during scrolling.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
struct ScrollGestureAxisLock
```

## Overview

When a scrollable view scrolls along both axes, the system can lock each scroll gesture to its predominant axis, so that a mostly vertical gesture scrolls only vertically. Pass a value of this type to the [`scrollGestureAxisLock(_:)`](./view/scrollgestureaxislock%28_%29.md) modifier.

## Topics

### Type Properties
- [static var automatic: ScrollGestureAxisLock](./scrollgestureaxislock/automatic.md)
  Uses the platform’s default behavior for locking scroll gestures.
- [static var directional: ScrollGestureAxisLock](./scrollgestureaxislock/directional.md)
  Scroll gestures are locked to their predominant axis.
- [static var disabled: ScrollGestureAxisLock](./scrollgestureaxislock/disabled.md)
  Scroll gestures can move along both axes at once.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollgestureaxislock)*