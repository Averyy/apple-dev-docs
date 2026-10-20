# CGPSConverter

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

An opaque data type used to convert PostScript data to PDF data.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
class CGPSConverter
```

```c
typedef struct CGPSConverter * CGPSConverterRef;
```

#### Overview

The PostScript data is supplied by a data provider and written into a data consumer. When you create a PostScript converter object, you can supply callback functions to invoke at various stages of the conversion process.

## Topics

### Initializers
- [init?(info: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGPSConverterCallbacks>, options: CFDictionary?)](./cgpsconverter/init%28info,callbacks,options%29.md)
  Creates a new PostScript converter.
### Instance Properties
- [var isConverting: Bool](./cgpsconverter/isconverting.md)
  Checks whether the converter is currently converting data.
### Type Properties
- [class var typeID: CFTypeID](./cgpsconverter/typeid.md)
  Returns the Core Foundation type identifier for PostScript converters.
### Instance Methods
- [func abort() -> Bool](./cgpsconverter/abort%28%29.md)
  Tells a PostScript converter to abort a conversion at the next available opportunity.
- [func convert(CGDataProvider, consumer: CGDataConsumer, options: CFDictionary?) -> Bool](./cgpsconverter/convert%28_,consumer,options%29.md)
  Uses a PostScript converter to convert PostScript data to PDF data.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverter)*