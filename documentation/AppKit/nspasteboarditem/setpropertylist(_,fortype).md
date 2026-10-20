# setPropertyList(_:forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the value for a specified type as a property list.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setPropertyList(_ propertyList: Any, forType type: NSPasteboard.PasteboardType) -> Bool
```

```objc
- (BOOL) setPropertyList:(id) propertyList forType:(NSPasteboardType) type;
```

#### Return Value

[`true`](../../Swift/true.md) if the value was set successfully, otherwise [`false`](../../Swift/false.md).

## Parameters

- `propertyList`: A property list object containing the value for the representation specified by `type`.
- `type`: A uniform type identifier string.

## See Also

### Setting values
- [func setData(Data, forType: NSPasteboard.PasteboardType) -> Bool](./setdata%28_,fortype%29.md)
  Sets the value for a specified type as a data object.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](./setstring%28_,fortype%29.md)
  Sets the value for a specified type as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/setpropertylist(_:fortype:))*