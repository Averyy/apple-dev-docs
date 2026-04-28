# CIVector

**Framework**: Core Image  
**Kind**: class

The Core Image class that defines a vector object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIVector
```

#### Overview

A `CIVector` can store one or more `CGFloat` in one object. They can store a group of float values for a variety of different uses such as coordinate points, direction vectors, geometric rectangles, transform matrices, convolution weights, or just a list a parameter values.

You use `CIVector` objects in conjunction with other Core Image classes, such as [`CIFilter`](cifilter-swift.class.md) and [`CIKernel`](cikernel.md).  Many of the built-in Core Image filters have one or more `CIVector` inputs that you can set to affect the filter’s behavior.

## Topics

### Initializing a Vector
- [init(values: UnsafePointer<CGFloat>, count: Int)](civector/init(values:count:).md)
  Initialize a Core Image vector object with the specified the values.
- [convenience init(x: CGFloat)](civector/init(x:).md)
  Initialize a Core Image vector object with one value.
- [convenience init(x: CGFloat, y: CGFloat)](civector/init(x:y:)-4grr.md)
  Initialize a Core Image vector object with two values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat)](civector/init(x:y:z:)-zais.md)
  Initialize a Core Image vector object with three values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](civector/init(x:y:z:w:)-75emo.md)
  Initialize a Core Image vector object with four values.
- [convenience init(string: String)](civector/init(string:).md)
  Initialize a Core Image vector object with values provided in a string representation.
- [convenience init(cgAffineTransform: CGAffineTransform)](civector/init(cgaffinetransform:)-6o8gl.md)
  Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](civector/init(cgpoint:)-8cf9j.md)
  Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](civector/init(cgrect:)-6bolw.md)
  Initialize a Core Image vector object with four values provided by a `CGRect` structure.
### Getting Values From a Vector
- [func value(at: Int) -> CGFloat](civector/value(at:).md)
  Returns a value from a specific position in the vector.
- [var count: Int](civector/count.md)
  The number of items in the vector.
- [var x: CGFloat](civector/x.md)
  The value located in the first position in the vector.
- [var y: CGFloat](civector/y.md)
  The value located in the second position in the vector.
- [var z: CGFloat](civector/z.md)
  The value located in the third position in the vector.
- [var w: CGFloat](civector/w.md)
  The value located in the forth position in the vector.
- [var stringRepresentation: String](civector/stringrepresentation.md)
  Returns a formatted string with all the values of a `CIVector`.
- [var cgAffineTransformValue: CGAffineTransform](civector/cgaffinetransformvalue.md)
  Returns the values in the vector as a `CGAffineTransformValue` structure.
- [var cgPointValue: CGPoint](civector/cgpointvalue.md)
  Returns the values in the vector as a `CGPoint` structure.
- [var cgRectValue: CGRect](civector/cgrectvalue.md)
  Returns the values in the vector as a `CGRect` structure.
### Initializers
- [convenience init(CGAffineTransform: CGAffineTransform)](civector/init(cgaffinetransform:)-61k8d.md)
- [convenience init(CGAffineTransform: CGAffineTransform)](civector/init(cgaffinetransform:)-gf61.md)
- [convenience init(CGPoint: CGPoint)](civector/init(cgpoint:)-2q3w0.md)
- [convenience init(CGPoint: CGPoint)](civector/init(cgpoint:)-339fj.md)
- [convenience init(CGRect: CGRect)](civector/init(cgrect:)-60mr0.md)
- [convenience init(CGRect: CGRect)](civector/init(cgrect:)-9l6dq.md)
- [init?(coder: NSCoder)](civector/init(coder:).md)
- [convenience init(x: CGFloat, Y: CGFloat)](civector/init(x:y:)-2ia98.md)
- [convenience init(x: CGFloat, Y: CGFloat)](civector/init(x:y:)-8ln4z.md)
- [convenience init(x: CGFloat, Y: CGFloat, Z: CGFloat)](civector/init(x:y:z:)-6pett.md)
- [convenience init(x: CGFloat, Y: CGFloat, Z: CGFloat)](civector/init(x:y:z:)-94o0c.md)
- [convenience init(x: CGFloat, Y: CGFloat, Z: CGFloat, W: CGFloat)](civector/init(x:y:z:w:)-3lp39.md)
- [convenience init(x: CGFloat, Y: CGFloat, Z: CGFloat, W: CGFloat)](civector/init(x:y:z:w:)-9obnr.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CIFilter](cifilter-swift.class.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIRAWFilter](cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIColor](cicolor.md)
  The Core Image class that defines a color object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector)*