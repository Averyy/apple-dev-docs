# permittedArrowDirections

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The arrow directions that you allow for the popover.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var permittedArrowDirections: UIPopoverArrowDirection { get set }
```

```objc
@property (nonatomic, assign) UIPopoverArrowDirection permittedArrowDirections;
```

## Discussion

Prior to displaying the popover, set this property to the arrow directions that you allow for your popover. The actual arrow direction in use by the popover is stored in the [`arrowDirection`](./arrowdirection.md) property.

The default value of this property is [`any`](../uipopoverarrowdirection/any.md).

## See Also

### Configuring the popover arrows
- [var arrowDirection: UIPopoverArrowDirection](./arrowdirection.md)
  The arrow direction in use by the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/permittedarrowdirections)*