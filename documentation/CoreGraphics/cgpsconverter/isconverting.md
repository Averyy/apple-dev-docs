# isConverting

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Checks whether the converter is currently converting data.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.3+

## Declaration

```swift
var isConverting: Bool { get }
```

```c
extern bool CGPSConverterIsConverting(CGPSConverterRef converter);
```

## See Also

### Miscellaneous Functions
- [CGPSConverterConvert](./convert%28_,consumer,options%29.md)
  Uses a PostScript converter to convert PostScript data to PDF data.
- [CGPSConverterAbort](./abort%28%29.md)
  Tells a PostScript converter to abort a conversion at the next available opportunity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverter/isconverting)*