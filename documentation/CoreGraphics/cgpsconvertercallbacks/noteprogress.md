# noteProgress

**Framework**: Core Graphics  
**Kind**: property

The callback called periodically during the conversion to indicate that conversion is proceeding, or `NULL`.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var noteProgress: CGPSConverterProgressCallback?
```

## See Also

- [var beginDocument: CGPSConverterBeginDocumentCallback?](cgpsconvertercallbacks/begindocument.md)
  The callback called at the beginning of the conversion of the PostScript document, or `NULL`.
- [var beginPage: CGPSConverterBeginPageCallback?](cgpsconvertercallbacks/beginpage.md)
  The callback called at the start of the conversion of each page in the PostScript document, or `NULL`.
- [var endDocument: CGPSConverterEndDocumentCallback?](cgpsconvertercallbacks/enddocument.md)
  The callback called at the end of conversion of the PostScript document, or `NULL`.
- [var endPage: CGPSConverterEndPageCallback?](cgpsconvertercallbacks/endpage.md)
  The callback called at the end of the conversion of each page in the PostScript document, or `NULL`.
- [var noteMessage: CGPSConverterMessageCallback?](cgpsconvertercallbacks/notemessage.md)
  The callback called to pass any messages that might result during the conversion, or `NULL`.
- [var releaseInfo: CGPSConverterReleaseInfoCallback?](cgpsconvertercallbacks/releaseinfo.md)
  The callback called when the converter is deallocated, or `NULL`.
- [var version: UInt32](cgpsconvertercallbacks/version.md)
  The version number of the structure passed in as a parameter to the converter creation functions. The structure defined below is version `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/noteprogress)*