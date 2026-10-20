# init(type:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a printer object initialized to the first available printer with the specified make and model information.

**Availability**:
- macOS

## Declaration

```swift
init?(type: NSPrinter.TypeName)
```

```objc
+ (NSPrinter *) printerWithType:(NSPrinterTypeName) type;
```

#### Return Value

An initialized `NSPrinter` object, or `nil` if the specified printer was not available.

## Parameters

- `type`: A string describing the make and model information. You can get this string using the [`printerTypes`](./printertypes.md) method.

## See Also

### Related Documentation
- [var type: NSPrinter.TypeName](./type.md)
  A description of the printer’s make and model.
### Creating the Printer Object
- [init?(name: String)](./init%28name%29.md)
  Creates and returns a printer object initialized with the specified printer name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/init(type:))*