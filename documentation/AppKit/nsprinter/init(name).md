# init(name:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a printer object initialized with the specified printer name.

**Availability**:
- macOS

## Declaration

```swift
init?(name: String)
```

```objc
+ (NSPrinter *) printerWithName:(NSString *) name;
```

#### Return Value

An initialized `NSPrinter` object, or `nil` if the specified printer was not available.

## Parameters

- `name`: The name of the printer.

## See Also

### Related Documentation
- [var name: String](./name.md)
  The printer’s name.
- [class NSPrinter](../nsprinter.md)
  An object that describes a printer’s capabilities.
- [class var printerNames: [String]](./printernames.md)
  Returns the names of all available printers.
### Creating the Printer Object
- [init?(type: NSPrinter.TypeName)](./init%28type%29.md)
  Creates and returns a printer object initialized to the first available printer with the specified make and model information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/init(name:))*