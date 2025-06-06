# item

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The app-specific item you want to share.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var item: Any { get }
```

#### Discussion

Use this property to provide the data you want to pass to the sharing service. The item must conform to the [`NSPasteboardWriting`](nspasteboardwriting.md) protocol, or be an [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) or [`NSDocument`](nsdocument.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspreviewrepresentableactivityitem/item)*