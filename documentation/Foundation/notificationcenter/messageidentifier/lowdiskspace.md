# lowDiskSpace

**Framework**: Foundation  
**Kind**: property

An identifier for a message about the available disk space getting low.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var lowDiskSpace: NotificationCenter.BaseMessageIdentifier<NSBundleResourceRequest.LowDiskSpaceMessage> { get }
```

#### Discussion

Use this identifier with [`NotificationCenter`](notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`NSBundleResourceRequest.LowDiskSpaceMessage`](nsbundleresourcerequest/lowdiskspacemessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/lowdiskspace)*