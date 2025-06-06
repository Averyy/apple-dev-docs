# propertyList(forType:)

**Framework**: AppKit  
**Kind**: method

Returns the value for the specified type as a property list.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func propertyList(forType type: NSPasteboard.PasteboardType) -> Any?
```

#### Return Value

The value for the specified type as a property list.

## Parameters

- `type`: A uniform type identifier string.

## See Also

- [func data(forType: NSPasteboard.PasteboardType) -> Data?](nspasteboarditem/data(fortype:).md)
  Returns the value for the specified type as a data object.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](nspasteboarditem/string(fortype:).md)
  Returns the value for the specified type as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/propertylist(fortype:))*