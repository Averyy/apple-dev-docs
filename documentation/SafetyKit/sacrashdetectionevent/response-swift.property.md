# response

**Framework**: SafetyKit  
**Kind**: property  
**Role**: Instance Property

An indication of whether the system attempted to call an Emergency SOS provider.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
var response: SACrashDetectionEvent.Response { get }
```

```objc
@property (nonatomic, readonly) SACrashDetectionEventResponse response;
```

## See Also

### Determining the event type
- [SACrashDetectionEvent.Response](./response-swift.enum.md)
  An enumeration that defines possible emergency responses to a Crash Detection event.
- [var date: Date](./date.md)
  The date and time the crash occurred.
- [var location: CLLocation?](./location.md)
  The longitude and latitude where the crash detection occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionevent/response-swift.property)*