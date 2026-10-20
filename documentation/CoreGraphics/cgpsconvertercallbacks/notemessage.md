# noteMessage

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

The callback called to pass any messages that might result during the conversion, or `NULL`.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var noteMessage: CGPSConverterMessageCallback?
```

```c
CGPSConverterMessageCallback noteMessage;
```

## See Also

### Instance Properties
- [var beginDocument: CGPSConverterBeginDocumentCallback?](./begindocument.md)
  The callback called at the beginning of the conversion of the PostScript document, or `NULL`.
- [var beginPage: CGPSConverterBeginPageCallback?](./beginpage.md)
  The callback called at the start of the conversion of each page in the PostScript document, or `NULL`.
- [var endDocument: CGPSConverterEndDocumentCallback?](./enddocument.md)
  The callback called at the end of conversion of the PostScript document, or `NULL`.
- [var endPage: CGPSConverterEndPageCallback?](./endpage.md)
  The callback called at the end of the conversion of each page in the PostScript document, or `NULL`.
- [var noteProgress: CGPSConverterProgressCallback?](./noteprogress.md)
  The callback called periodically during the conversion to indicate that conversion is proceeding, or `NULL`.
- [var releaseInfo: CGPSConverterReleaseInfoCallback?](./releaseinfo.md)
  The callback called when the converter is deallocated, or `NULL`.
- [var version: UInt32](./version.md)
  The version number of the structure passed in as a parameter to the converter creation functions. The structure defined below is version `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/notemessage)*