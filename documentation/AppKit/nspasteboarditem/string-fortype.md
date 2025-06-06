# string(forType:)

**Framework**: AppKit  
**Kind**: method

Returns the value for the specified type as a string.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func string(forType type: NSPasteboard.PasteboardType) -> String?
```

#### Return Value

The value for the specified type as a string.

## Parameters

- `type`: A uniform type identifier string.

## See Also

- [func data(forType: NSPasteboard.PasteboardType) -> Data?](nspasteboarditem/data(fortype:).md)
  Returns the value for the specified type as a data object.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](nspasteboarditem/propertylist(fortype:).md)
  Returns the value for the specified type as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/string(fortype:))*