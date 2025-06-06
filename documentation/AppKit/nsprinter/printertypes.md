# printerTypes

**Framework**: AppKit  
**Kind**: property

Returns descriptions of the makes and models of all available printers.

**Availability**:
- macOS ?+

## Declaration

```swift
class var printerTypes: [NSPrinter.TypeName] { get }
```

#### Return Value

An array of `NSString` objects, each of which contains the make and model information for a supported printer.

## See Also

- [var type: NSPrinter.TypeName](nsprinter/type.md)
  A description of the printer’s make and model.
- [class var printerNames: [String]](nsprinter/printernames.md)
  Returns the names of all available printers.
- [NSPrinter.TypeName](nsprinter/typename.md)
  The type you use to describe a printer’s make and model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/printertypes)*