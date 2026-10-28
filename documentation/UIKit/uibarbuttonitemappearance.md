# UIBarButtonItemAppearance

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object for customizing the appearance of bar button items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIBarButtonItemAppearance
```

```objc
@interface UIBarButtonItemAppearance : NSObject
```

## Overview

Use a [`UIBarButtonItemAppearance`](./uibarbuttonitemappearance.md) object to customize the appearance of a bar button item in each of its possible states. You can customize the appearance differently for different states. For example, you might apply different colors to the button’s title in the [`normal`](./uibarbuttonitemappearance/normal.md) and [`highlighted`](./uibarbuttonitemappearance/highlighted.md) states.

## Topics

### Creating a bar button item appearance object
- [init(style: UIBarButtonItem.Style)](./uibarbuttonitemappearance/init%28style%29.md)
  Creates an appearance with default values that are appropriate for the specified button style.
- [convenience init()](./uibarbuttonitemappearance/init%28%29.md)
  Creates an appearance object with default values that are appropriate for a plain button.
- [init(coder: NSCoder)](./uibarbuttonitemappearance/init%28coder%29.md)
  Creates an appearance object from data in an unarchiver.
### Copying a bar button item bar appearance object
- [func copy() -> Self](./uibarbuttonitemappearance/copy%28%29.md)
  Creates a copy of the appearance object.
### Resetting the appearance properties
- [func configureWithDefault(for: UIBarButtonItem.Style)](./uibarbuttonitemappearance/configurewithdefault%28for%29.md)
  Configures the bar button item appearance object with appropriate values for the specified button style.
### Configuring attributes for different button states
- [var normal: UIBarButtonItemStateAppearance](./uibarbuttonitemappearance/normal.md)
  The appearance data to apply to the button when it’s in the normal state.
- [var disabled: UIBarButtonItemStateAppearance](./uibarbuttonitemappearance/disabled.md)
  The appearance data to apply to the button when it’s in the disabled state.
- [var highlighted: UIBarButtonItemStateAppearance](./uibarbuttonitemappearance/highlighted.md)
  The appearance data to apply to the button when it’s in the highlighted state.
- [var focused: UIBarButtonItemStateAppearance](./uibarbuttonitemappearance/focused.md)
  The appearance data to apply to the button when it’s focused.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Shared appearance
- [class UIBarAppearance](./uibarappearance.md)
  An object for customizing the basic appearance of system bars.
- [class UIBarButtonItemStateAppearance](./uibarbuttonitemstateappearance.md)
  A data object containing the specific customizations for a bar button item in a particular state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemappearance)*