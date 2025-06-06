# union(_:)

**Framework**: AppKit  
**Kind**: method

Creates a new compression options object representing the union with the provided options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func union(_ options: NSUserInterfaceCompressionOptions) -> NSUserInterfaceCompressionOptions
```

#### Return Value

A new `NSCompressibleUserInterfaceOptions` object which represents the union with the supplied compression options.

## Parameters

- `options`: A set of compression options to add to the current object.

## See Also

- [func subtracting(NSUserInterfaceCompressionOptions) -> NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions/subtracting(_:).md)
  Creates a new compression options object with the supplied options removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/union(_:))*