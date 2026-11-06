# UIBarContainerBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Whether this navigation controller acts as a bar container, reading the bar content of its child view controller and rendering that content in the navigation controller’s own bar.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
enum UIBarContainerBehavior
```

```c
enum UIBarContainerBehavior : NSInteger;
```

## Overview

For example, if there is a split view controller where one of the columns is a view controller with multiple child `UINavigationController`s, set `barContainerBehavior` to `.local` on all the children so that each one renders its own bar, instead of their toolbar content being rendered in a single toolbar managed by the split view controller.

Defaults to `.automatic`.

## Topics

### Enumeration Cases
- [UIBarContainerBehavior.automatic](./uibarcontainerbehavior/automatic.md)
  The system decides whether this navigation controller renders the bar, or whether its bar content should be integrated into a single bar in a parent container view controller, like a split view controller.
- [UIBarContainerBehavior.local](./uibarcontainerbehavior/local.md)
  This navigation controller reads the bar content of its child view controllers and always renders a distinct, local bar.
### Initializers
- [init?(rawValue: Int)](./uibarcontainerbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarcontainerbehavior)*