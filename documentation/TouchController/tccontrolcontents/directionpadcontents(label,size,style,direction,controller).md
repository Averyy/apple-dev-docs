# directionPadContents(label:size:style:direction:controller:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Type Method

The direction pad contents for the specified label, size, style, and direction.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class func directionPadContents(label: TCControlLabel, size: CGSize, style: TCControlContents.DpadElementStyle, direction: TCControlContents.DpadDirection, controller: TCTouchController) -> TCControlContents
```

```objc
+ (TCControlContents *) directionPadContentsForLabel:(TCControlLabel *) label size:(CGSize) size style:(TCControlContentsDpadElementStyle) style direction:(TCControlContentsDpadDirection) direction controller:(TCTouchController *) controller;
```

## Return Value

The `TCControlContents` for the direction pad.

## Parameters

- `label`: The label for the direction pad.
- `size`: The size of the direction pad in points.
- `style`: The style of the direction pad.
- `direction`: The direction of the direction pad visual.
- `controller`: The touch controller to create control contents for.

## See Also

### Accessing directional pad contents
- [TCControlContents.DpadDirection](./dpaddirection.md)
  Defines the direction of a direction pad visual.
- [TCControlContents.DpadElementStyle](./dpadelementstyle.md)
  Defines the visual style of the individual up/down/left/right elements of a direction pad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/directionpadcontents(label:size:style:direction:controller:))*