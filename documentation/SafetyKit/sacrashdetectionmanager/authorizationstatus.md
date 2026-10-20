# authorizationStatus

**Framework**: SafetyKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates if the person authorized the app to receive Crash Detection events.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
var authorizationStatus: SAAuthorizationStatus { get }
```

```objc
@property (nonatomic, readonly) SAAuthorizationStatus authorizationStatus;
```

## See Also

### Determining availability
- [class var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates if Crash Detection is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager/authorizationstatus)*