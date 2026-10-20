# NSAccessibilityImage

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A role-based protocol that declares the minimum interface necessary for an accessibility element to act as an image.

**Availability**:
- macOS

## Declaration

```swift
protocol NSAccessibilityImage : NSAccessibilityElementProtocol
```

```objc
@protocol NSAccessibilityImage <NSAccessibilityElement>
```

#### Overview

Use this protocol when you want a user interface element to behave like an image_ _in the accessibility hierarchy.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md) protocol declares.

> **Explicit Implementation Required**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Topics

### Supporting Accessibility
- [func accessibilityLabel() -> String?](./nsaccessibilityimage/accessibilitylabel%28%29.md)
  Returns a short description of the image’s label.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSImageView](./nsimageview.md)

## See Also

### Images and Color
- [protocol NSAccessibilityColor](./nsaccessibilitycolor.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityimage)*