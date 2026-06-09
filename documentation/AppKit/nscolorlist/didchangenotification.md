# didChangeNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever a color list changes.

**Availability**:
- macOS ?+

## Declaration

```swift
class let didChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is the [`NSColorList`](nscolorlist.md) object that changed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSColorList.DidChangeMessage`](nscolorlist/didchangemessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/didchangenotification)*