# isPruned

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether the system removes some push notification content before delivery.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isPruned: Bool { get }
```

#### Discussion

The server may truncate the payload data of a push notification if the size of that data exceeds the allowed maximum. For notifications you create using a payload dictionary, the value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the payload data doesn’t contain all information regarding the change. The value is [`false`](https://developer.apple.com/documentation/swift/false) if the payload data is complete.

For notifications you fetch from the database using a `CKFetchNotificationChangesOperation` operation, this property’s value is always [`true`](https://developer.apple.com/documentation/swift/true).

When CloudKit must remove payload data, it removes it in a specific order. This class’s properties are among the last that CloudKit removes because they define information about how to deliver the push notification. The following list shows the properties that CloudKit removes, and the order for removing them:

1. [`containerIdentifier`](cknotification/containeridentifier.md)
2. Keys that subclasses of `CKNotification` define.
3. [`soundName`](cknotification/soundname.md)
4. [`alertLaunchImage`](cknotification/alertlaunchimage.md)
5. [`alertActionLocalizationKey`](cknotification/alertactionlocalizationkey.md)
6. [`alertBody`](cknotification/alertbody.md)
7. [`alertLocalizationArgs`](cknotification/alertlocalizationargs.md)
8. [`alertLocalizationKey`](cknotification/alertlocalizationkey.md)
9. [`badge`](cknotification/badge.md)
10. [`notificationID`](cknotification/notificationid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/ispruned)*