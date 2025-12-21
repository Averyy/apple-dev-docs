# delegate

**Framework**: SafetyKit  
**Kind**: property

The object that receives Crash Detection events.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
weak var delegate: (any SACrashDetectionDelegate)? { get set }
```

## See Also

- [func requestAuthorization(completionHandler: (SAAuthorizationStatus, (any Error)?) -> Void)](sacrashdetectionmanager/requestauthorization(completionhandler:).md)
  Requests permission to access Crash Detection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager/delegate)*