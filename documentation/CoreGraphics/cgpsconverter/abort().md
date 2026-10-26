# abort()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Tells a PostScript converter to abort a conversion at the next available opportunity.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.3+

## Declaration

```swift
func abort() -> Bool
```

```c
extern bool CGPSConverterAbort(CGPSConverterRef converter);
```

#### Return Value

A Boolean value that indicates whether the converter is currently converting data (`true` if it is).

## See Also

### Instance Methods
- [func convert(CGDataProvider, consumer: CGDataConsumer, options: CFDictionary?) -> Bool](./convert%28_,consumer,options%29.md)
  Uses a PostScript converter to convert PostScript data to PDF data.
### Miscellaneous Functions
- [CGPSConverterIsConverting](./isconverting.md)
  Checks whether the converter is currently converting data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverter/abort())*