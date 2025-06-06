# data(forType:)

**Framework**: AppKit  
**Kind**: method

Returns the value for the specified type as a data object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func data(forType type: NSPasteboard.PasteboardType) -> Data?
```

#### Return Value

The value for the specified type as an `NSData` object.

## Parameters

- `type`: A uniform type identifier string.

## See Also

- [func string(forType: NSPasteboard.PasteboardType) -> String?](nspasteboarditem/string(fortype:).md)
  Returns the value for the specified type as a string.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](nspasteboarditem/propertylist(fortype:).md)
  Returns the value for the specified type as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/data(fortype:))*