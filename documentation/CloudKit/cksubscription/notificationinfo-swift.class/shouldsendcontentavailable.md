# shouldSendContentAvailable

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the push notification includes the content available flag.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var shouldSendContentAvailable: Bool { get set }
```

```objc
@property (assign) BOOL shouldSendContentAvailable;
```

#### Discussion

When this property is [`true`](../../../Swift/true.md), the server includes the `content-available` flag in the push notification’s payload. That flag causes the system to wake or launch an app that isn’t currently running. The app then receives background execution time to download any data for the push notification, such as the set of changed records. If the app is already running in the foreground, the inclusion of this flag has no additional effect and the system delivers the notification to the app delegate for processing as usual.

The default value of this property is [`false`](../../../Swift/false.md).

## See Also

### Accessing the Notification Info
- [var shouldSendMutableContent: Bool](./shouldsendmutablecontent.md)
  A Boolean value that indicates whether the push notification sets the mutable content flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/shouldsendcontentavailable)*