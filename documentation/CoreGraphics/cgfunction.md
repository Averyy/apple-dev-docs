# CGFunction

**Framework**: Core Graphics  
**Kind**: class

A general facility for defining and using callback functions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CGFunction
```

#### Overview

These functions can take an arbitrary number of floating-point input values and pass back an arbitrary number of floating-point output values.

Core Graphics uses function objects to implement shadings. [`CGShading`](cgshading.md) describes the parameters and semantics required for the callbacks used by function objects.

## Topics

### Creating Function Objects
- [init?(info: UnsafeMutableRawPointer?, domainDimension: Int, domain: UnsafePointer<CGFloat>?, rangeDimension: Int, range: UnsafePointer<CGFloat>?, callbacks: UnsafePointer<CGFunctionCallbacks>)](cgfunction/init(info:domaindimension:domain:rangedimension:range:callbacks:).md)
  Creates a Core Graphics function.
### Callbacks
- [struct CGFunctionCallbacks](cgfunctioncallbacks.md)
  A structure that contains callbacks needed by a `CGFunctionRef` object.
- [typealias CGFunctionEvaluateCallback](cgfunctionevaluatecallback.md)
  Performs custom operations on the supplied input data to produce output data.
- [typealias CGFunctionReleaseInfoCallback](cgfunctionreleaseinfocallback.md)
  Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgfunction/typeid.md)
  Returns the type identifier for Core Graphics function objects.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [class CGDataConsumer](cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [class CGDataProvider](cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [class CGShading](cgshading.md)
  A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [class CGGradient](cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [class CGPattern](cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunction)*