# userActivityForCancelingInApplication

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A user activity object for canceling the ride request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var userActivityForCancelingInApplication: NSUserActivity? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readwrite, nullable) NSUserActivity * userActivityForCancelingInApplication;
```

*macOS*

```objc
@property (atomic, strong, readwrite, nullable) NSUserActivity * userActivityForCancelingInApplication;
```

## Discussion

If the user asks to cancel a ride that hasn’t completed, the system checks the value of this property. If you provided an appropriate [`NSUserActivity`](../../Foundation/nsuseractivity.md) object, the system launches your app and asks it to continue with that object. The object you provide should include the information your app needs to cancel the ride request.

Upon receiving this user activity object, your app should display a confirmation UI to the user asking them to confirm the cancellation request. If the user confirms the request, you may proceed to cancel the ride request.

The default value of this property is `nil`.

## See Also

### Providing User Activity Objects
- [var additionalActionActivities: [NSUserActivity]?](./additionalactionactivities.md)
  Additional activities that the user may choose to perform while the ride request is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/useractivityforcancelinginapplication)*