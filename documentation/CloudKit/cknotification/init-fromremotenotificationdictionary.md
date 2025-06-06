# init(fromRemoteNotificationDictionary:)

**Framework**: CloudKit  
**Kind**: init

Creates a new notification using the specified payload data.

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
convenience init?(fromRemoteNotificationDictionary notificationDictionary: [AnyHashable : Any])
```

## Parameters

- `notificationDictionary`: The push notification’s payload data. Use the dictionary that the system provides to your app delegate’s   method. This parameter must not be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/init(fromremotenotificationdictionary:))*