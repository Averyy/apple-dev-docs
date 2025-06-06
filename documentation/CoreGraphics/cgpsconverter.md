# CGPSConverter

**Framework**: Core Graphics  
**Kind**: class

An opaque data type used to convert PostScript data to PDF data.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
class CGPSConverter
```

#### Overview

The PostScript data is supplied by a data provider and written into a data consumer. When you create a PostScript converter object, you can supply callback functions to invoke at various stages of the conversion process.

## Topics

### Initializers
- [init?(info: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGPSConverterCallbacks>, options: CFDictionary?)](cgpsconverter/init(info:callbacks:options:).md)
  Creates a new PostScript converter.
### Instance Properties
- [var isConverting: Bool](cgpsconverter/isconverting.md)
  Checks whether the converter is currently converting data.
### Type Properties
- [class var typeID: CFTypeID](cgpsconverter/typeid.md)
  Returns the Core Foundation type identifier for PostScript converters.
### Instance Methods
- [func abort() -> Bool](cgpsconverter/abort.md)
  Tells a PostScript converter to abort a conversion at the next available opportunity.
- [func convert(CGDataProvider, consumer: CGDataConsumer, options: CFDictionary?) -> Bool](cgpsconverter/convert(_:consumer:options:).md)
  Uses a PostScript converter to convert PostScript data to PDF data.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverter)*