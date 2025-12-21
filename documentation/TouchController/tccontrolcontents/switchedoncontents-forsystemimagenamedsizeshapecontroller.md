# switchedOnContents(forSystemImageNamed:size:shape:controller:)

**Framework**: Touch Controller  
**Kind**: method

The switch contents for the specified system image name, size, and shape.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class func switchedOnContents(forSystemImageNamed imageName: String, size: CGSize, shape: TCControlContents.ButtonShape, controller: TCTouchController) -> TCControlContents
```

#### Return Value

The `TCControlContents` for the switch button.

## Parameters

- `imageName`: The name of the system image to use for the switch button.
- `size`: The size of the switch button in points.
- `shape`: The shape of the switch button.
- `controller`: The touch controller to create control contents for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/switchedoncontents(forsystemimagenamed:size:shape:controller:))*