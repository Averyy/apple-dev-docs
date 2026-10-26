# pageSize(forPaper:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the size of the page for the specified paper type.

**Availability**:
- macOS

## Declaration

```swift
func pageSize(forPaper paperName: NSPrinter.PaperName) -> NSSize
```

```objc
- (NSSize) pageSizeForPaper:(NSPrinterPaperName) paperName;
```

#### Return Value

The size of the page, measured in points in the user coordinate space. The returned size is zero if the specified paper name is not recognized or its entry in the PPD file cannot be parsed.

## Parameters

- `paperName`: Possible values are printer-dependent and are contained in the printer’s PPD file. Typical values are “Letter” and “Legal”.

## See Also

### Getting Page and Printer Information
- [NSPrinter.PaperName](./papername.md)
  The type you use to specify the name of a type of paper.
- [var languageLevel: Int](./languagelevel.md)
  The PostScript language level recognized by the printer.
### Related Documentation
- [- imageRectForPaper:](./imagerectforpaper_.md)
  Deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/pagesize(forpaper:))*