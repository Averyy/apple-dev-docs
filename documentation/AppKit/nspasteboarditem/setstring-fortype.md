# setString(_:forType:)

**Framework**: AppKit  
**Kind**: method

Sets the value for a specified type as a string.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setString(_ string: String, forType type: NSPasteboard.PasteboardType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the value was set successfully, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `string`: A string for the representation specified by  .
- `type`: A uniform type identifier string.

## See Also

- [func setData(Data, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboarditem/setdata(_:fortype:).md)
  Sets the value for a specified type as a data object.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboarditem/setpropertylist(_:fortype:).md)
  Sets the value for a specified type as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/setstring(_:fortype:))*