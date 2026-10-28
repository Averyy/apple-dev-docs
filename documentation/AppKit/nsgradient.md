# NSGradient

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that can draw gradient fill colors

**Availability**:
- macOS 10.5+

## Declaration

```swift
class NSGradient
```

```objc
@interface NSGradient : NSObject
```

## Overview

This class provides convenience methods for drawing radial or linear (axial) gradients for rectangles and [`NSBezierPath`](./nsbezierpath.md) objects. It also supports primitive methods that let you customize the shape of the gradient fill. A gradient consists of two or more color changes over the range of the gradient shape. When creating a gradient object, you specify the colors and their locations relative to the start and end of the gradient. This combination of color and location is known as a *color stop*. During drawing, the [`NSGradient`](./nsgradient.md) object uses the color stop information to compute color changes for you and passes that information to the Quartz shading functions.

Because the [`NSGradient`](./nsgradient.md) class uses Quartz shadings, drawing is handled by computing the colors at a given point mathematically. This technique results in smooth gradients regardless of the resolution of the target device.

For more information about gradients and their appearance, see [Gradients](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_shadings/dq_shadings.html#//apple_ref/doc/uid/TP30001066-CH207) in [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## Topics

### Creating a Gradient
- [convenience init?(starting: NSColor, ending: NSColor)](./nsgradient/init%28starting,ending%29.md)
  Initializes a newly allocated gradient object with two colors.
- [convenience init?(colors: [NSColor])](./nsgradient/init%28colors%29.md)
  Initializes a newly allocated gradient object with an array of colors.
- [convenience init?(colorsAndLocations: (NSColor, CGFloat)...)](./nsgradient/init%28colorsandlocations%29.md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.
- [init?(colors: [NSColor], atLocations: UnsafePointer<CGFloat>?, colorSpace: NSColorSpace)](./nsgradient/init%28colors,atlocations,colorspace%29.md)
  Initializes a newly allocated gradient object with the specified colors, color locations, and color space.
- [init?(coder: NSCoder)](./nsgradient/init%28coder%29.md)
  Creates a gradient from data in an unarchiver.
- [- initWithColorsAndLocations:](./nsgradient/initwithcolorsandlocations_.md)
  Initializes a newly allocated gradient object with a comma-separated list of arguments.
### Drawing a Linear Gradient
- [func draw(from: NSPoint, to: NSPoint, options: NSGradient.DrawingOptions)](./nsgradient/draw%28from,to,options%29.md)
  Draws a linear gradient between the specified start and end points.
- [func draw(in: NSRect, angle: CGFloat)](./nsgradient/draw%28in,angle%29-7sdyh.md)
  Fills the specified rectangle with a linear gradient.
- [func draw(in: NSBezierPath, angle: CGFloat)](./nsgradient/draw%28in,angle%29-68adz.md)
  Fills the specified path with a linear gradient.
### Drawing a Radial Gradient
- [func draw(fromCenter: NSPoint, radius: CGFloat, toCenter: NSPoint, radius: CGFloat, options: NSGradient.DrawingOptions)](./nsgradient/draw%28fromcenter,radius,tocenter,radius,options%29.md)
  Draws a radial gradient between the specified circles.
- [func draw(in: NSRect, relativeCenterPosition: NSPoint)](./nsgradient/draw%28in,relativecenterposition%29-3a83.md)
  Draws a radial gradient starting at the center of the specified rectangle.
- [func draw(in: NSBezierPath, relativeCenterPosition: NSPoint)](./nsgradient/draw%28in,relativecenterposition%29-502cc.md)
  Draws a radial gradient starting at the center point of the specified path.
### Getting Gradient Properties
- [var colorSpace: NSColorSpace](./nsgradient/colorspace.md)
  The color space of the colors associated with the gradient.
- [var numberOfColorStops: Int](./nsgradient/numberofcolorstops.md)
  The number of color stops associated with the gradient.
- [func getColor(AutoreleasingUnsafeMutablePointer<NSColor>?, location: UnsafeMutablePointer<CGFloat>?, at: Int)](./nsgradient/getcolor%28_,location,at%29.md)
  Returns information about the color stop at the specified index in the receiver’s color array.
- [func interpolatedColor(atLocation: CGFloat) -> NSColor](./nsgradient/interpolatedcolor%28atlocation%29.md)
  Returns the color of the rendered gradient at the specified relative location.
### Constants
- [NSGradient.DrawingOptions](./nsgradient/drawingoptions.md)
  Constants that specify gradient drawing options.
### Initializers
- [convenience init?(startingColor: NSColor, endingColor: NSColor)](./nsgradient/init%28startingcolor,endingcolor%29.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient)*