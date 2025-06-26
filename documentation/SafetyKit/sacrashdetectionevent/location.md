# location

**Framework**: SafetyKit  
**Kind**: property

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

## See Also

- [SACrashDetectionEvent.Response](sacrashdetectionevent/response-swift.enum.md)
  An enumeration that defines possible emergency responses to a Crash Detection event.
- [var date: Date](sacrashdetectionevent/date.md)
  The date and time the crash occurred.
- [var response: SACrashDetectionEvent.Response](sacrashdetectionevent/response-swift.property.md)
  An indication of whether the system attempted to call an Emergency SOS provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionevent/location)*