# init(info:callbacks:options:)

**Framework**: Core Graphics  
**Kind**: init

Creates a new PostScript converter.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.3+

## Declaration

```swift
init?(info: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGPSConverterCallbacks>, options: CFDictionary?)
```

#### Return Value

A new PostScript converter, or `NULL` if a converter could not be created. You are responsible for releasing this object.

## Parameters

- `info`: A pointer to the data that will be passed to the callbacks.
- `callbacks`: A pointer to a PostScript converter callbacks structure that specifies the callbacks to be used during a conversion process.
- `options`: This parameter should be  ; it is reserved for future expansion of the API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverter/init(info:callbacks:options:))*