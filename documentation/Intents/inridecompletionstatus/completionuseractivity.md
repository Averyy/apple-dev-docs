# completionUserActivity

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user activity object indicating any additional steps the user needs to be take in your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var completionUserActivity: NSUserActivity? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readwrite, nullable) NSUserActivity * completionUserActivity;
```

*macOS*

```objc
@property (atomic, strong, readwrite, nullable) NSUserActivity * completionUserActivity;
```

## Discussion

Providing an object in this property lets the system know that it should prompt the user to open your app when the ride reaches the [`INRidePhase.completed`](../inridephase/completed.md) phase. In the user activity object, include any information needed to communicate what steps the user still needs to take. For example, you might include information to let your app know that payment is still required or that it should ask the user to provide feedback on the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/completionuseractivity)*