# setData(_:forType:)

**Framework**: AppKit  
**Kind**: method

Sets the value for a specified type as a data object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setData(_ data: Data, forType type: NSPasteboard.PasteboardType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the value was set successfully, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `data`: An   object containing the value for the representation specified by  .
- `type`: A uniform type identifier string.

## See Also

- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboarditem/setstring(_:fortype:).md)
  Sets the value for a specified type as a string.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboarditem/setpropertylist(_:fortype:).md)
  Sets the value for a specified type as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/setdata(_:fortype:))*