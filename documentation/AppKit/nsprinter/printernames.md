# printerNames

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the names of all available printers.

**Availability**:
- macOS

## Declaration

```swift
class var printerNames: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * printerNames;
```

## Return Value

An array of `NSString` objects, each of which contains the name of an available printer.

## Discussion

The user constructs the list of available printers when adding a printer in the Print panel or setting up printers in the Print & Scan preferences pane.

## See Also

### Related Documentation
- [var name: String](./name.md)
  The printer’s name.
### Getting General Printer Information
- [class var printerTypes: [NSPrinter.TypeName]](./printertypes.md)
  Returns descriptions of the makes and models of all available printers.
- [NSPrinter.TypeName](./typename.md)
  The type you use to describe a printer’s make and model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/printernames)*