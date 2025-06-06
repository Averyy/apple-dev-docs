# languageLevel

**Framework**: AppKit  
**Kind**: property

The PostScript language level recognized by the printer.

**Availability**:
- macOS ?+

## Declaration

```swift
var languageLevel: Int { get }
```

#### Return Value

The PostScript language level. The value is 0 if the receiver is not a PostScript printer.

## See Also

- [func pageSize(forPaper: NSPrinter.PaperName) -> NSSize](nsprinter/pagesize(forpaper:).md)
  Returns the size of the page for the specified paper type.
- [NSPrinter.PaperName](nsprinter/papername.md)
  The type you use to specify the name of a type of paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/languagelevel)*