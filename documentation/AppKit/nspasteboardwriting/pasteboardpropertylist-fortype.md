# pasteboardPropertyList(forType:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a property list object to represent the receiver on a pasteboard as an object of a specified type.

**Availability**:
- macOS ?+

## Declaration

```swift
func pasteboardPropertyList(forType type: NSPasteboard.PasteboardType) -> Any?
```

#### Return Value

A property list object to represent the receiver on a pasteboard as an object of type `type`.

#### Discussion

The returned value will commonly be the `NSData` object for the specified data type. However, if this method returns either a string, or any other property-list type, the pasteboard will automatically convert these items to the correct data format required for the pasteboard.

## Parameters

- `type`: One of the types the receiver supports for writing (one of the UTIs returned by its implementation of  ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardwriting/pasteboardpropertylist(fortype:))*