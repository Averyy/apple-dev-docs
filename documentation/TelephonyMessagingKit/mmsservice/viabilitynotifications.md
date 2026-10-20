# viabilityNotifications

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

An asynchronous sequence of service viability notifications produced by the service.

**Availability**:
- iOS 26.0+

## Declaration

```swift
final var viabilityNotifications: some AsyncSequence<MMSService.ViabilityNotification, Never> { get throws }
```

#### Discussion

Use a `for`-`await`-`in` loop to receive [`MMSService.ViabilityNotification`](./viabilitynotification.md) instances from this property.

## See Also

### Determining service viabililty
- [func isViable(for: CellularServiceID) -> Bool](./isviable%28for%29.md)
  Queries whether the device can perform MMS operations at this time.
- [MMSService.ViabilityNotification](./viabilitynotification.md)
  A notification that indicates if MMS is viable for a given cellular service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/viabilitynotifications)*