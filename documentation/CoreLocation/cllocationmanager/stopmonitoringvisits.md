# stopMonitoringVisits()

**Framework**: Core Location  
**Kind**: method

Stops the delivery of visit-related events.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
func stopMonitoringVisits()
```

#### Discussion

Calling this method disables the delivery of visit-related events for your app. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

- [func startMonitoringVisits()](cllocationmanager/startmonitoringvisits.md)
  Starts the delivery of visit-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/stopmonitoringvisits())*