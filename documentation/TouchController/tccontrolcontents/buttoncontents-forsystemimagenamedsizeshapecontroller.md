# buttonContents(forSystemImageNamed:size:shape:controller:)

**Framework**: Touch Controller  
**Kind**: method

The button contents for the specified system image name, size, and shape.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class func buttonContents(forSystemImageNamed imageName: String, size: CGSize, shape: TCControlContents.ButtonShape, controller: TCTouchController) -> TCControlContents
```

#### Return Value

The `TCControlContents` for the button.

## Parameters

- `imageName`: The name of the system image to use for the button.
- `size`: The size of the button in points.
- `shape`: The shape of the button.
- `controller`: The touch controller to create control contents for.

## See Also

- [TCControlContents.ButtonShape](tccontrolcontents/buttonshape.md)
  Defines the visual shape of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/buttoncontents(forsystemimagenamed:size:shape:controller:))*