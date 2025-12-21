# contains(_:)

**Framework**: AppKit  
**Kind**: method

Determines whether the supplied compression options are all present in the current instance.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func contains(_ options: NSUserInterfaceCompressionOptions) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if all the supplied options are present in the instance’s options, or [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## Parameters

- `options`: A compression options object to compare with the current instance.

## See Also

- [var isEmpty: Bool](nsuserinterfacecompressionoptions/isempty.md)
  A Boolean value that denotes whether the option is empty.
- [func intersects(NSUserInterfaceCompressionOptions) -> Bool](nsuserinterfacecompressionoptions/intersects(_:).md)
  Determines whether the supplied compression options intersect with the current instance’s options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions/contains(_:))*