# setPropertyList(_:forType:)

**Framework**: AppKit  
**Kind**: method

Sets the value for a specified type as a property list.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setPropertyList(_ propertyList: Any, forType type: NSPasteboard.PasteboardType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the value was set successfully, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `propertyList`: A property list object containing the value for the representation specified by  .
- `type`: A uniform type identifier string.

## See Also

- [func setData(Data, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboarditem/setdata(_:fortype:).md)
  Sets the value for a specified type as a data object.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboarditem/setstring(_:fortype:).md)
  Sets the value for a specified type as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/setpropertylist(_:fortype:))*