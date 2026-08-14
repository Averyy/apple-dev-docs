# NSPrinter.TypeName

**Framework**: AppKit  
**Kind**: struct

The type you use to describe a printer’s make and model.

**Availability**:
- macOS ?+

## Declaration

```swift
struct TypeName
```

## Topics

### Initializers
- [init(String)](nsprinter/typename/init(_:).md)
  Creates a printer type name.
- [init(rawValue: String)](nsprinter/typename/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class var printerNames: [String]](nsprinter/printernames.md)
  Returns the names of all available printers.
- [class var printerTypes: [NSPrinter.TypeName]](nsprinter/printertypes.md)
  Returns descriptions of the makes and models of all available printers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/typename)*