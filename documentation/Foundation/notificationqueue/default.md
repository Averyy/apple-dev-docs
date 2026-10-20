# default

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns the default notification queue for the current thread.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var `default`: NotificationQueue { get }
```

```objc
@property (class, strong, readonly) NSNotificationQueue * defaultQueue;
```

#### Return Value

Returns the default notification queue for the current thread.

#### Discussion

This notification queue uses the default notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/default)*