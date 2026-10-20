# previewRepresentableActivityItems(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

A collection of Preview-representable activity items, used for sharing and collaboration.

**Availability**:
- macOS 13.2+

## Declaration

```swift
@MainActor
optional func previewRepresentableActivityItems(for window: NSWindow) -> [any NSPreviewRepresentableActivityItem]?
```

```objc
- (NSArray<id<NSPreviewRepresentableActivityItem>> *) previewRepresentableActivityItemsForWindow:(NSWindow *) window;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/previewrepresentableactivityitems(for:))*