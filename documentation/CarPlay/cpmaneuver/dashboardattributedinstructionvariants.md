# dashboardAttributedInstructionVariants

**Framework**: CarPlay  
**Kind**: property

An array of attributed instruction variants for the CarPlay dashboard.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var dashboardAttributedInstructionVariants: [NSAttributedString] { get set }
```

#### Discussion

Localize each variant for display to the user, and make sure the array has at least one variant. The system displays the first variant that fits into the available screen space, so arrange the variants in order from most- to least-preferred.

> **Note**:  If you provide both [`dashboardInstructionVariants`](cpmaneuver/dashboardinstructionvariants.md) and [`dashboardAttributedInstructionVariants`](cpmaneuver/dashboardattributedinstructionvariants.md), the system displays instructions from the attributed instruction variants array.

The attributed strings in the array can have only a single attribute—an [`NSTextAttachment`](https://developer.apple.com/documentation/uikit/nstextattachment). CarPlay removes all other attributes.

Using a text attachment attribute, you can add an image to a maneuver instruction as the example below shows. The maximum text attachment image size is 64 x 16 points.

Listing 1.

**Swift**:

```swift
let instruction = NSMutableAttributedString(string: "Turn right on Apple Park Way")

// Attach an image.
let image = UIImage(systemName: "arrow.turn.up.right")!
let attachment = NSTextAttachment(image: image)
let container = NSAttributedString(attachment: attachment)

instruction.append(container)
```

**Obj-C**:

```objc
NSMutableAttributedString *instruction = [[NSMutableAttributedString alloc]
                                              initWithString:@"Turn right on Apple Park Way"];

// Attach an image.
UIImage *image = [UIImage systemImageNamed:@"arrow.turn.up.right"];
NSTextAttachment *attachment = [NSTextAttachment textAttachmentWithImage:image];
NSAttributedString *container = [NSAttributedString attributedStringWithAttachment:attachment];
    
[instruction appendAttributedString:container];
```

## See Also

- [var attributedInstructionVariants: [NSAttributedString]](cpmaneuver/attributedinstructionvariants.md)
  An array of attributed instruction variants for the maneuver.
- [var notificationAttributedInstructionVariants: [NSAttributedString]](cpmaneuver/notificationattributedinstructionvariants.md)
  An array of attributed instruction variants for notification banners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/dashboardattributedinstructionvariants)*