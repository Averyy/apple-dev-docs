# abort()

**Framework**: Core Graphics  
**Kind**: method

Tells a PostScript converter to abort a conversion at the next available opportunity.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.3+

## Declaration

```swift
func abort() -> Bool
```

#### Return Value

A Boolean value that indicates whether the converter is currently converting data (`true` if it is).

## See Also

- [func convert(CGDataProvider, consumer: CGDataConsumer, options: CFDictionary?) -> Bool](cgpsconverter/convert(_:consumer:options:).md)
  Uses a PostScript converter to convert PostScript data to PDF data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverter/abort())*