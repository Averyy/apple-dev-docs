# authorizationStatus

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Returns your app’s current ability to access the user’s focus status.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var authorizationStatus: INFocusStatusAuthorizationStatus { get }
```

```objc
@property (nonatomic, readonly) INFocusStatusAuthorizationStatus authorizationStatus;
```

## See Also

### Requesting Authorization
- [func requestAuthorization(completionHandler: ((INFocusStatusAuthorizationStatus) -> Void)?)](./requestauthorization%28completionhandler%29.md)
  Asks the system for access to the user’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infocusstatuscenter/authorizationstatus)*