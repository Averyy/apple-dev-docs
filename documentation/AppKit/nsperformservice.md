# NSPerformService(_:_:)

**Framework**: AppKit  
**Kind**: func

Programmatically invokes a Services menu service.

**Availability**:
- macOS ?+

## Declaration

```swift
func NSPerformService(_ itemName: String, _ pboard: NSPasteboard?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the service was successfully performed or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not.

#### Discussion

Use this function to programmatically invoke a service found in the application’s Services menu.

## Parameters

- `itemName`: Specifies a Services menu item, in any language. If the requested service is from a submenu of the Services menu, the value must contain a slash (for example, “Mail/Selection”).
- `pboard`: The pasteboard containing the data required by the service. This data must be present for the service to succeed. On output, this pasteboard contains the data returned by the service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsperformservice(_:_:))*