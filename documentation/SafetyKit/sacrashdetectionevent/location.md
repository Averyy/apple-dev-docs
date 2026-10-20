# location

**Framework**: SafetyKit  
**Kind**: property  
**Role**: Instance Property

The longitude and latitude where the crash detection occurred.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
var location: CLLocation? { get }
```

```objc
@property (nonatomic, readonly, nullable) CLLocation * location;
```

## See Also

### Determining the event type
- [SACrashDetectionEvent.Response](./response-swift.enum.md)
  An enumeration that defines possible emergency responses to a Crash Detection event.
- [var date: Date](./date.md)
  The date and time the crash occurred.
- [var response: SACrashDetectionEvent.Response](./response-swift.property.md)
  An indication of whether the system attempted to call an Emergency SOS provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionevent/location)*