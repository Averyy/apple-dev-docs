# setData(_:forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the value for a specified type as a data object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setData(_ data: Data, forType type: NSPasteboard.PasteboardType) -> Bool
```

```objc
- (BOOL) setData:(NSData *) data forType:(NSPasteboardType) type;
```

#### Return Value

[`true`](../../Swift/true.md) if the value was set successfully, otherwise [`false`](../../Swift/false.md).

## Parameters

- `data`: An `NSData` object containing the value for the representation specified by `type`.
- `type`: A uniform type identifier string.

## See Also

### Setting values
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](./setstring%28_,fortype%29.md)
  Sets the value for a specified type as a string.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](./setpropertylist%28_,fortype%29.md)
  Sets the value for a specified type as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/setdata(_:fortype:))*