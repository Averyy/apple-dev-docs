# delegate

**Framework**: SafetyKit  
**Kind**: property  
**Role**: Instance Property

The object that receives Crash Detection events.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
weak var delegate: (any SACrashDetectionDelegate)? { get set }
```

```objc
@property (nonatomic, weak, readwrite) id<SACrashDetectionDelegate> delegate;
```

## See Also

### Requesting authorization
- [func requestAuthorization(completionHandler: (SAAuthorizationStatus, (any Error)?) -> Void)](./requestauthorization%28completionhandler%29.md)
  Requests permission to access Crash Detection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager/delegate)*