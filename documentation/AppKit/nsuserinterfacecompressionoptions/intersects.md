# intersects(_:)

**Framework**: AppKit  
**Kind**: method

Determines whether the supplied compression options intersect with the current instance’s options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func intersects(_ options: NSUserInterfaceCompressionOptions) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if at least one of the supplied options is present in the instance’s options, or [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `options`: A compression options object to compare with the current instance.

## See Also

- [var isEmpty: Bool](nsuserinterfacecompressionoptions/isempty.md)
  A Boolean value that denotes whether the option is empty.
- [func contains(NSUserInterfaceCompressionOptions) -> Bool](nsuserinterfacecompressionoptions/contains(_:).md)
  Determines whether the supplied compression options are all present in the current instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/intersects(_:))*