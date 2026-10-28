# printerTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns descriptions of the makes and models of all available printers.

**Availability**:
- macOS

## Declaration

```swift
class var printerTypes: [NSPrinter.TypeName] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * printerTypes;
```

## Return Value

An array of `NSString` objects, each of which contains the make and model information for a supported printer.

## See Also

### Related Documentation
- [var type: NSPrinter.TypeName](./type.md)
  A description of the printer’s make and model.
### Getting General Printer Information
- [class var printerNames: [String]](./printernames.md)
  Returns the names of all available printers.
- [NSPrinter.TypeName](./typename.md)
  The type you use to describe a printer’s make and model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/printertypes)*