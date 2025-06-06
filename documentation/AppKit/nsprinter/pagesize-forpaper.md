# pageSize(forPaper:)

**Framework**: AppKit  
**Kind**: method

Returns the size of the page for the specified paper type.

**Availability**:
- macOS ?+

## Declaration

```swift
func pageSize(forPaper paperName: NSPrinter.PaperName) -> NSSize
```

#### Return Value

The size of the page, measured in points in the user coordinate space. The returned size is zero if the specified paper name is not recognized or its entry in the PPD file cannot be parsed.

## Parameters

- `paperName`: Possible values are printer-dependent and are contained in the printer’s PPD file. Typical values are “Letter” and “Legal”.

## See Also

- [NSPrinter.PaperName](nsprinter/papername.md)
  The type you use to specify the name of a type of paper.
- [var languageLevel: Int](nsprinter/languagelevel.md)
  The PostScript language level recognized by the printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/pagesize(forpaper:))*