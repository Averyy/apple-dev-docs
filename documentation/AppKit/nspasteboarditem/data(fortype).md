# data(forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value for the specified type as a data object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func data(forType type: NSPasteboard.PasteboardType) -> Data?
```

```objc
- (NSData *) dataForType:(NSPasteboardType) type;
```

#### Return Value

The value for the specified type as an `NSData` object.

## Parameters

- `type`: A uniform type identifier string.

## See Also

### Getting values
- [func string(forType: NSPasteboard.PasteboardType) -> String?](./string%28fortype%29.md)
  Returns the value for the specified type as a string.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](./propertylist%28fortype%29.md)
  Returns the value for the specified type as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/data(fortype:))*