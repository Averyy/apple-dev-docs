# NSAffineTransform

**Framework**: Foundation  
**Kind**: class

A graphics coordinate transformation.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSAffineTransform
```

#### Overview

In Swift, this object bridges to [`AffineTransform`](affinetransform.md); use [`NSAffineTransform`](nsaffinetransform.md) when you need reference semantics or other Foundation-specific behavior.

A transformation specifies how points in one coordinate system are transformed to points in another coordinate system. An affine transformation is a special type of transformation that preserves parallel lines in a path but does not necessarily preserve lengths or angles. Scaling, rotation, and translation are the most commonly used manipulations supported by affine transforms, but shearing is also possible.

> **Note**:  In OS X 10.3 and earlier the [`NSAffineTransform`](nsaffinetransform.md) class was declared and implemented entirely in the Application Kit framework. As of macOS 10.4 the [`NSAffineTransform`](nsaffinetransform.md) class has been split across the Foundation and Application Kit frameworks.

 In OS X 10.3 and earlier the [`NSAffineTransform`](nsaffinetransform.md) class was declared and implemented entirely in the Application Kit framework. As of macOS 10.4 the [`NSAffineTransform`](nsaffinetransform.md) class has been split across the Foundation and Application Kit frameworks.

Methods for applying affine transformations to the current graphics context and a method for applying an affine transformation to an [`NSBezierPath`](https://developer.apple.com/documentation/AppKit/NSBezierPath) object are described in NSAffineTransform Additions Reference in the Application Kit.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`AffineTransform`](affinetransform.md) structure, which bridges to the [`NSAffineTransform`](nsaffinetransform.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`AffineTransform`](affinetransform.md) structure, which bridges to the [`NSAffineTransform`](nsaffinetransform.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Creating an Affine Transform
- [init()](nsaffinetransform/init.md)
  Initializes an affine transform matrix to the identity matrix.
- [convenience init(transform: NSAffineTransform)](nsaffinetransform/init(transform:).md)
  Initializes the receiver’s matrix using another transform object.
### Accumulating Transformations
- [func rotate(byDegrees: Double)](nsaffinetransform/rotate(bydegrees:).md)
  Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [func rotate(byRadians: Double)](nsaffinetransform/rotate(byradians:).md)
  Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [func scale(by: Double)](nsaffinetransform/scale(by:).md)
  Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [func scaleX(by: Double, yBy: Double)](nsaffinetransform/scalex(by:yby:).md)
  Applies scaling factors to each axis of the receiver’s transformation matrix.
- [func translateX(by: Double, yBy: Double)](nsaffinetransform/translatex(by:yby:).md)
  Applies the specified translation factors to the receiver’s transformation matrix.
- [func append(NSAffineTransform)](nsaffinetransform/append(_:).md)
  Appends the specified matrix to the receiver’s matrix.
- [func prepend(NSAffineTransform)](nsaffinetransform/prepend(_:).md)
  Prepends the specified matrix to the receiver’s matrix.
- [func invert()](nsaffinetransform/invert.md)
  Replaces the receiver’s matrix with its inverse matrix.
### Transforming Data and Objects
- [func transform(NSPoint) -> NSPoint](nsaffinetransform/transform(_:)-41p16.md)
  Applies the receiver’s transform to the specified point and returns the result.
- [func transform(NSSize) -> NSSize](nsaffinetransform/transform(_:)-5r6ol.md)
  Applies the receiver’s transform to the specified size and returns the results.
- [func transform(NSBezierPath) -> NSBezierPath](nsaffinetransform/transform(_:)-6z1xo.md)
  Creates and returns a new [`NSBezierPath`](https://developer.apple.com/documentation/AppKit/NSBezierPath) object with each point in the given path transformed by the receiver.
### Accessing the Transformation Matrix
- [var transformStruct: NSAffineTransformStruct](nsaffinetransform/transformstruct.md)
  The matrix coefficients stored as the transformation matrix.
- [struct NSAffineTransformStruct](nsaffinetransformstruct.md)
  A structure that defines the three-by-three matrix that performs an affine transform between two coordinate systems.
### Setting and Building the Current Transformation Matrix
- [func set()](nsaffinetransform/set.md)
  Sets the current transformation matrix to the receiver’s transformation matrix.
- [func concat()](nsaffinetransform/concat.md)
  Appends the receiver’s matrix to the current transformation matrix stored in the current graphics context, replacing the current transformation matrix with the result.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform)*