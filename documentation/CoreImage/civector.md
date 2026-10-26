# CIVector

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

The Core Image class that defines a vector object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class CIVector
```

```objc
@interface CIVector : NSObject
```

#### Overview

A `CIVector` can store one or more `CGFloat` in one object. They can store a group of float values for a variety of different uses such as coordinate points, direction vectors, geometric rectangles, transform matrices, convolution weights, or just a list a parameter values.

You use `CIVector` objects in conjunction with other Core Image classes, such as [`CIFilter`](./cifilter-swift.class.md) and [`CIKernel`](./cikernel.md).  Many of the built-in Core Image filters have one or more `CIVector` inputs that you can set to affect the filter’s behavior.

## Topics

### Creating a Vector
- [convenience init(cgAffineTransform: CGAffineTransform)](./civector/init%28cgaffinetransform%29-59e4k.md)
  Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](./civector/init%28cgpoint%29-3mobm.md)
  Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](./civector/init%28cgrect%29-3undj.md)
  Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.
- [+ vectorWithValues:count:](./civector/vectorwithvalues_count_.md)
  Create a Core Image vector object that is initialized with the specified values.
- [+ vectorWithX:](./civector/vectorwithx_.md)
  Create a Core Image vector object that is initialized with one value.
- [+ vectorWithX:Y:](./civector/vectorwithx_y_.md)
  Create a Core Image vector object that is initialized with two values.
- [+ vectorWithX:Y:Z:](./civector/vectorwithx_y_z_.md)
  Create a Core Image vector object that is initialized with three values.
- [+ vectorWithX:Y:Z:W:](./civector/vectorwithx_y_z_w_.md)
  Create a Core Image vector object that is initialized with four values.
- [+ vectorWithString:](./civector/vectorwithstring_.md)
  Create a Core Image vector object with values provided in a string representation.
### Initializing a Vector
- [init(values: UnsafePointer<CGFloat>, count: Int)](./civector/init%28values,count%29.md)
  Initialize a Core Image vector object with the specified the values.
- [convenience init(x: CGFloat)](./civector/init%28x%29.md)
  Initialize a Core Image vector object with one value.
- [convenience init(x: CGFloat, y: CGFloat)](./civector/init%28x,y%29-4grr.md)
  Initialize a Core Image vector object with two values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat)](./civector/init%28x,y,z%29-zais.md)
  Initialize a Core Image vector object with three values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](./civector/init%28x,y,z,w%29-75emo.md)
  Initialize a Core Image vector object with four values.
- [convenience init(string: String)](./civector/init%28string%29.md)
  Initialize a Core Image vector object with values provided in a string representation.
- [convenience init(cgAffineTransform: CGAffineTransform)](./civector/init%28cgaffinetransform%29-6o8gl.md)
  Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](./civector/init%28cgpoint%29-8cf9j.md)
  Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](./civector/init%28cgrect%29-6bolw.md)
  Initialize a Core Image vector object with four values provided by a `CGRect` structure.
### Getting Values From a Vector
- [func value(at: Int) -> CGFloat](./civector/value%28at%29.md)
  Returns a value from a specific position in the vector.
- [var count: Int](./civector/count.md)
  The number of items in the vector.
- [var x: CGFloat](./civector/x.md)
  The value located in the first position in the vector.
- [var y: CGFloat](./civector/y.md)
  The value located in the second position in the vector.
- [var z: CGFloat](./civector/z.md)
  The value located in the third position in the vector.
- [var w: CGFloat](./civector/w.md)
  The value located in the forth position in the vector.
- [var stringRepresentation: String](./civector/stringrepresentation.md)
  Returns a formatted string with all the values of a `CIVector`.
- [var cgAffineTransformValue: CGAffineTransform](./civector/cgaffinetransformvalue.md)
  Returns the values in the vector as a `CGAffineTransformValue` structure.
- [var cgPointValue: CGPoint](./civector/cgpointvalue.md)
  Returns the values in the vector as a `CGPoint` structure.
- [var cgRectValue: CGRect](./civector/cgrectvalue.md)
  Returns the values in the vector as a `CGRect` structure.
### Initializers
- [convenience init(CGAffineTransform: CGAffineTransform)](./civector/init%28cgaffinetransform%29-61k8d.md)
- [convenience init(CGAffineTransform: CGAffineTransform)](./civector/init%28cgaffinetransform%29-gf61.md)
- [convenience init(CGPoint: CGPoint)](./civector/init%28cgpoint%29-2q3w0.md)
- [convenience init(CGPoint: CGPoint)](./civector/init%28cgpoint%29-339fj.md)
- [convenience init(CGRect: CGRect)](./civector/init%28cgrect%29-60mr0.md)
- [convenience init(CGRect: CGRect)](./civector/init%28cgrect%29-9l6dq.md)
- [init?(coder: NSCoder)](./civector/init%28coder%29.md)
- [convenience init(x: CGFloat, Y: CGFloat)](./civector/init%28x,y%29-2ia98.md)
- [convenience init(x: CGFloat, Y: CGFloat)](./civector/init%28x,y%29-8ln4z.md)
- [convenience init(x: CGFloat, Y: CGFloat, Z: CGFloat)](./civector/init%28x,y,z%29-6pett.md)
- [convenience init(x: CGFloat, Y: CGFloat, Z: CGFloat)](./civector/init%28x,y,z%29-94o0c.md)
- [convenience init(x: CGFloat, Y: CGFloat, Z: CGFloat, W: CGFloat)](./civector/init%28x,y,z,w%29-3lp39.md)
- [convenience init(x: CGFloat, Y: CGFloat, Z: CGFloat, W: CGFloat)](./civector/init%28x,y,z,w%29-9obnr.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Filters
- [class CIFilter](./cifilter-swift.class.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIRAWFilter](./cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIColor](./cicolor.md)
  The Core Image class that defines a color object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector)*