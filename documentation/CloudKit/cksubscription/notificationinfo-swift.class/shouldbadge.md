# shouldBadge

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether an app’s icon badge increments its value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var shouldBadge: Bool { get set }
```

```objc
@property (assign) BOOL shouldBadge;
```

## Discussion

The default value of this property is [`false`](../../../Swift/false.md). Set it to [`true`](../../../Swift/true.md) to cause the system to increment the badge value whenever it receives the corresponding push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/shouldbadge)*