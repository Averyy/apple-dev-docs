# CGPSConverterBeginPageCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

Performs custom tasks at the beginning of each page in a PostScript conversion process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias CGPSConverterBeginPageCallback = (UnsafeMutableRawPointer?, Int, CFDictionary) -> Void
```

```c
typedef void (*)(void *, unsigned long, const struct __CFDictionary *) CGPSConverterBeginPageCallback;
```

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(info:callbacks:options:)`](./cgpsconverter/init%28info,callbacks,options%29.md).
- `pageNumber`: The current page number. Page numbers start at `1`.
- `pageInfo`: A dictionary that contains contextual information about the page. This parameter is reserved for future API expansion, and is currently unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterbeginpagecallback)*