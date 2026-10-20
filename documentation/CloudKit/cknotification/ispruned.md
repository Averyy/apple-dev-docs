# isPruned

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system removes some push notification content before delivery.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isPruned: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL isPruned;
```

#### Discussion

The server may truncate the payload data of a push notification if the size of that data exceeds the allowed maximum. For notifications you create using a payload dictionary, the value of this property is [`true`](../../Swift/true.md) if the payload data doesn’t contain all information regarding the change. The value is [`false`](../../Swift/false.md) if the payload data is complete.

For notifications you fetch from the database using a `CKFetchNotificationChangesOperation` operation, this property’s value is always [`true`](../../Swift/true.md).

When CloudKit must remove payload data, it removes it in a specific order. This class’s properties are among the last that CloudKit removes because they define information about how to deliver the push notification. The following list shows the properties that CloudKit removes, and the order for removing them:

1. [`containerIdentifier`](./containeridentifier.md)
2. Keys that subclasses of `CKNotification` define.
3. [`soundName`](./soundname.md)
4. [`alertLaunchImage`](./alertlaunchimage.md)
5. [`alertActionLocalizationKey`](./alertactionlocalizationkey.md)
6. [`alertBody`](./alertbody.md)
7. [`alertLocalizationArgs`](./alertlocalizationargs.md)
8. [`alertLocalizationKey`](./alertlocalizationkey.md)
9. [`badge`](./badge.md)
10. [`notificationID`](./notificationid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/ispruned)*