# attributedInstructionVariants

**Framework**: CarPlay  
**Kind**: property

An array of attributed instruction variants for the maneuver.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var attributedInstructionVariants: [NSAttributedString] { get set }
```

#### Discussion

Localize each variant for display to the user, and make sure the array has at least one variant. The system displays the first variant that fits into the available screen space, so arrange the variants in order from most- to least-preferred.

> **Note**:  If you provide both [`instructionVariants`](cpmaneuver/instructionvariants.md) and [`attributedInstructionVariants`](cpmaneuver/attributedinstructionvariants.md), the system displays instructions from the attributed instruction variants array.

The attributed strings in the array can have only a single attribute—an [`NSTextAttachment`](https://developer.apple.com/documentation/UIKit/NSTextAttachment). CarPlay removes all other attributes.

Using a text attachment attribute, you can add an image to a maneuver instruction as the example below shows. The maximum text attachment image size is 64 x 16 points.

Listing 1.

## See Also

- [var dashboardAttributedInstructionVariants: [NSAttributedString]](cpmaneuver/dashboardattributedinstructionvariants.md)
  An array of attributed instruction variants for the CarPlay dashboard.
- [var notificationAttributedInstructionVariants: [NSAttributedString]](cpmaneuver/notificationattributedinstructionvariants.md)
  An array of attributed instruction variants for notification banners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/attributedinstructionvariants)*