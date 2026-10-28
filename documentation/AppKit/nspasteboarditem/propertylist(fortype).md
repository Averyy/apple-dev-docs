# propertyList(forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value for the specified type as a property list.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func propertyList(forType type: NSPasteboard.PasteboardType) -> Any?
```

```objc
- (id) propertyListForType:(NSPasteboardType) type;
```

## Return Value

The value for the specified type as a property list.

## Parameters

- `type`: A uniform type identifier string.

## See Also

### Getting values
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](./data%28fortype%29.md)
  Returns the value for the specified type as a data object.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](./string%28fortype%29.md)
  Returns the value for the specified type as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/propertylist(fortype:))*