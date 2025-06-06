# printerNames

**Framework**: AppKit  
**Kind**: property

Returns the names of all available printers.

**Availability**:
- macOS ?+

## Declaration

```swift
class var printerNames: [String] { get }
```

#### Return Value

An array of `NSString` objects, each of which contains the name of an available printer.

#### Discussion

The user constructs the list of available printers when adding a printer in the Print panel or setting up printers in the Print & Scan preferences pane.

## See Also

- [var name: String](nsprinter/name.md)
  The printer’s name.
- [class var printerTypes: [NSPrinter.TypeName]](nsprinter/printertypes.md)
  Returns descriptions of the makes and models of all available printers.
- [NSPrinter.TypeName](nsprinter/typename.md)
  The type you use to describe a printer’s make and model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/printernames)*