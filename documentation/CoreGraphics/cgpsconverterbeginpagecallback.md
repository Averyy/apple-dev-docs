# CGPSConverterBeginPageCallback

**Framework**: Core Graphics  
**Kind**: typealias

Performs custom tasks at the beginning of each page in a PostScript conversion process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias CGPSConverterBeginPageCallback = (UnsafeMutableRawPointer?, Int, CFDictionary) -> Void
```

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to  .
- `pageNumber`: The current page number. Page numbers start at  .
- `pageInfo`: A dictionary that contains contextual information about the page. This parameter is reserved for future API expansion, and is currently unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterbeginpagecallback)*