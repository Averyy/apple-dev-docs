# UIBarMinimizationSafeAreaAdjustment

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum UIBarMinimizationSafeAreaAdjustment
```

```c
enum UIBarMinimizationSafeAreaAdjustment : NSInteger;
```

## Topics

### Adjusting the safe area
- [UIBarMinimizationSafeAreaAdjustment.automatic](./uibarminimizationsafeareaadjustment/automatic.md)
  The system determines the safe area adjustment.
- [UIBarMinimizationSafeAreaAdjustment.disabled](./uibarminimizationsafeareaadjustment/disabled.md)
  The safe area remains unchanged as bars minimize.
- [UIBarMinimizationSafeAreaAdjustment.enabled](./uibarminimizationsafeareaadjustment/enabled.md)
  The safe area adjusts as bars minimize, allowing content to reflow.
### Creating a safe area adjustment
- [init?(rawValue: Int)](./uibarminimizationsafeareaadjustment/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [UIAccessibility.ExpandedStatus](./uiaccessibility/expandedstatus.md)
- [UITextFormattingViewController.ComponentSize](./uitextformattingviewcontroller/componentsize.md)
  Sizes of text formatting view controller components.
- [enum UIFocusItemDeferralMode](./uifocusitemdeferralmode.md)
- [enum UIBarMinimizationBehavior](./uibarminimizationbehavior.md)
- [enum UIBarMinimizationRestorationBehavior](./uibarminimizationrestorationbehavior.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarminimizationsafeareaadjustment)*