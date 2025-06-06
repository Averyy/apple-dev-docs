# convert(_:to:)

**Framework**: Core Animation  
**Kind**: method

Converts the point from the receiver’s coordinate system to the specified layer’s coordinate system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func convert(_ p: CGPoint, to l: CALayer?) -> CGPoint
```

#### Return Value

The point converted to the coordinate system of `layer`.

#### Discussion

If you specify `nil` for the `l` parameter, this method returns the original point added to the layer’s frame’s origin.

The following example shows code that creates two layers, `redLayer` and `yellowLayer`. `yellowLayer` is scaled so that it is half of its original size.

```swift
let layerFrame = CGRect(x: 0, y: 0, width: 640, height: 480)
     
let redLayer = CALayer()
redLayer.frame = layerFrame
redLayer.backgroundColor = UIColor.red.cgColor
     
let yellowLayer = CALayer()
yellowLayer.frame = layerFrame
yellowLayer.backgroundColor = UIColor.yellow.cgColor
yellowLayer.transform = CATransform3DMakeScale(0.5, 0.5, 1)
```

The following figure shows the two layers and an overlaid point (rendered as a blue cross) with a position of `(50.0, 50.0)` in the red layer’s coordinate system.

![Layers with different coordinate systems](https://docs-assets.developer.apple.com/published/39fed9ba00d48f3636301f0d02be529d/media-2850332%402x.png)

The following code shows how you can find the coordinates of that point in the yellow layer’s coordinate system.

```swift
let position = CGPoint(x: 50, y: 50)
print(redLayer.convert(position, to: yellowLayer))
```

## Parameters

- `p`: A point specifying a location in the coordinate system of  .
- `l`: The layer into whose coordinate system   is to be converted. The receiver and   must share a common parent layer. This parameter may be  .

## See Also

- [func convert(CGPoint, from: CALayer?) -> CGPoint](calayer/convert(_:from:)-8kl76.md)
  Converts the point from the specified layer’s coordinate system to the receiver’s coordinate system.
- [func convert(CGRect, from: CALayer?) -> CGRect](calayer/convert(_:from:)-4kx9l.md)
  Converts the rectangle from the specified layer’s coordinate system to the receiver’s coordinate system.
- [func convert(CGRect, to: CALayer?) -> CGRect](calayer/convert(_:to:)-tly5.md)
  Converts the rectangle from the receiver’s coordinate system to the specified layer’s coordinate system.
- [func convertTime(CFTimeInterval, from: CALayer?) -> CFTimeInterval](calayer/converttime(_:from:).md)
  Converts the time interval from the specified layer’s time space to the receiver’s time space.
- [func convertTime(CFTimeInterval, to: CALayer?) -> CFTimeInterval](calayer/converttime(_:to:).md)
  Converts the time interval from the receiver’s time space to the specified layer’s time space


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/convert(_:to:)-7dcke)*