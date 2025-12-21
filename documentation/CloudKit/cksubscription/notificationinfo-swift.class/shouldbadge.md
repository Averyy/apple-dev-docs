# shouldBadge

**Framework**: CloudKit  
**Kind**: property

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

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). Set it to [`true`](https://developer.apple.com/documentation/Swift/true) to cause the system to increment the badge value whenever it receives the corresponding push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/shouldbadge)*