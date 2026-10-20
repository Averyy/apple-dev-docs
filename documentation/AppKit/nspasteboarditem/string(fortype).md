# string(forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value for the specified type as a string.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func string(forType type: NSPasteboard.PasteboardType) -> String?
```

```objc
- (NSString *) stringForType:(NSPasteboardType) type;
```

#### Return Value

The value for the specified type as a string.

## Parameters

- `type`: A uniform type identifier string.

## See Also

### Getting values
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](./data%28fortype%29.md)
  Returns the value for the specified type as a data object.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](./propertylist%28fortype%29.md)
  Returns the value for the specified type as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/string(fortype:))*