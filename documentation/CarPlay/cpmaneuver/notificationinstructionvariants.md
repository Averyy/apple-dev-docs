# notificationInstructionVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of instruction variants for notification banners.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var notificationInstructionVariants: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * notificationInstructionVariants;
```

## Discussion

Localize each variant for display to the user, and make sure the array contains at least one variant. The system displays the first variant that fits into the available screen space, so arrange the variants in order from most- to least-preferred.

> **Note**:  If you provide both [`notificationInstructionVariants`](./notificationinstructionvariants.md) and [`notificationAttributedInstructionVariants`](./notificationattributedinstructionvariants.md), the system displays instructions from the attributed instruction variants array. If you don’t provide notification variants, the system checks for [`attributedInstructionVariants`](./attributedinstructionvariants.md), and then [`instructionVariants`](./instructionvariants.md).

## See Also

### Providing instructions
- [var dashboardInstructionVariants: [String]](./dashboardinstructionvariants.md)
  An array of instruction variants for the CarPlay dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/notificationinstructionvariants)*