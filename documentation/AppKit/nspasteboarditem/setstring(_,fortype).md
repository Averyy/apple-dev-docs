# setString(_:forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the value for a specified type as a string.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setString(_ string: String, forType type: NSPasteboard.PasteboardType) -> Bool
```

```objc
- (BOOL) setString:(NSString *) string forType:(NSPasteboardType) type;
```

## Return Value

[`true`](../../Swift/true.md) if the value was set successfully, otherwise [`false`](../../Swift/false.md).

## Parameters

- `string`: A string for the representation specified by `type`.
- `type`: A uniform type identifier string.

## See Also

### Setting values
- [func setData(Data, forType: NSPasteboard.PasteboardType) -> Bool](./setdata%28_,fortype%29.md)
  Sets the value for a specified type as a data object.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](./setpropertylist%28_,fortype%29.md)
  Sets the value for a specified type as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/setstring(_:fortype:))*