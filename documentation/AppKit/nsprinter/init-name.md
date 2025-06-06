# init(name:)

**Framework**: AppKit  
**Kind**: init

Creates and returns a printer object initialized with the specified printer name.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(name: String)
```

#### Return Value

An initialized `NSPrinter` object, or `nil` if the specified printer was not available.

## Parameters

- `name`: The name of the printer.

## See Also

- [var name: String](nsprinter/name.md)
  The printer’s name.
- [Printing Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_aboutprinting/osxp_aboutprt.html#//apple_ref/doc/uid/10000083i)
- [class var printerNames: [String]](nsprinter/printernames.md)
  Returns the names of all available printers.
- [init?(type: NSPrinter.TypeName)](nsprinter/init(type:).md)
  Creates and returns a printer object initialized to the first available printer with the specified make and model information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/init(name:))*