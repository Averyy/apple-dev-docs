# init(type:)

**Framework**: AppKit  
**Kind**: init

Creates and returns a printer object initialized to the first available printer with the specified make and model information.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(type: NSPrinter.TypeName)
```

#### Return Value

An initialized `NSPrinter` object, or `nil` if the specified printer was not available.

## Parameters

- `type`: A string describing the make and model information. You can get this string using the   method.

## See Also

- [var type: NSPrinter.TypeName](nsprinter/type.md)
  A description of the printer’s make and model.
- [init?(name: String)](nsprinter/init(name:).md)
  Creates and returns a printer object initialized with the specified printer name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/init(type:))*