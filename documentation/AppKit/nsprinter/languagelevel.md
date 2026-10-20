# languageLevel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The PostScript language level recognized by the printer.

**Availability**:
- macOS

## Declaration

```swift
var languageLevel: Int { get }
```

```objc
@property (readonly) NSInteger languageLevel;
```

#### Return Value

The PostScript language level. The value is 0 if the receiver is not a PostScript printer.

## See Also

### Getting Page and Printer Information
- [func pageSize(forPaper: NSPrinter.PaperName) -> NSSize](./pagesize%28forpaper%29.md)
  Returns the size of the page for the specified paper type.
- [NSPrinter.PaperName](./papername.md)
  The type you use to specify the name of a type of paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/languagelevel)*