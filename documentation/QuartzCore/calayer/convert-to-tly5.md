# convert(_:to:)

**Framework**: Core Animation  
**Kind**: method

Converts the rectangle from the receiver’s coordinate system to the specified layer’s coordinate system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func convert(_ r: CGRect, to l: CALayer?) -> CGRect
```

#### Return Value

The rectangle converted to the coordinate system of `l`.

#### Discussion

If you specify `nil` for the `l` parameter, this method returns the original rect with an origin added to the layer’s frame’s origin.

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

The following figure shows the two layers and an overlaid rectangle with a frame of `(50, 50, 200, 200)` in the red layer’s coordinate system.

![Layers with different coordinate systems](https://docs-assets.developer.apple.com/published/04558faab052c26b463625dbc8c7cc46/media-2850323%402x.png)

The following code shows how you can find the coordinates of that rectangle in the yellow layer’s coordinate system.

```swift
let rect = CGRect(x: 50, y: 50, width: 200, height: 200)
print(redLayer.convert(rect, to: yellowLayer)) // prints (-220.0, -140.0, 400.0, 400.0)
```

## Parameters

- `r`: A point specifying a location in the coordinate system of  .
- `l`: The layer into whose coordinate system   is to be converted. The receiver and   and must share a common parent layer. This parameter may be  .

## See Also

- [func convert(CGPoint, from: CALayer?) -> CGPoint](calayer/convert(_:from:)-8kl76.md)
  Converts the point from the specified layer’s coordinate system to the receiver’s coordinate system.
- [func convert(CGPoint, to: CALayer?) -> CGPoint](calayer/convert(_:to:)-7dcke.md)
  Converts the point from the receiver’s coordinate system to the specified layer’s coordinate system.
- [func convert(CGRect, from: CALayer?) -> CGRect](calayer/convert(_:from:)-4kx9l.md)
  Converts the rectangle from the specified layer’s coordinate system to the receiver’s coordinate system.
- [func convertTime(CFTimeInterval, from: CALayer?) -> CFTimeInterval](calayer/converttime(_:from:).md)
  Converts the time interval from the specified layer’s time space to the receiver’s time space.
- [func convertTime(CFTimeInterval, to: CALayer?) -> CFTimeInterval](calayer/converttime(_:to:).md)
  Converts the time interval from the receiver’s time space to the specified layer’s time space


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/convert(_:to:)-tly5)*