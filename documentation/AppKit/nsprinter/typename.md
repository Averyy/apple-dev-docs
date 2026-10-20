# NSPrinter.TypeName

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The type you use to describe a printer’s make and model.

**Availability**:
- macOS

## Declaration

```swift
struct TypeName
```

```c
typedef NSString * NSPrinterTypeName;
```

## Topics

### Initializers
- [init(String)](./typename/init%28_%29.md)
  Creates a printer type name.
- [init(rawValue: String)](./typename/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting General Printer Information
- [class var printerNames: [String]](./printernames.md)
  Returns the names of all available printers.
- [class var printerTypes: [NSPrinter.TypeName]](./printertypes.md)
  Returns descriptions of the makes and models of all available printers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/typename)*