# stopMonitoringVisits()

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) stopMonitoringVisits;
```

## Discussion

Calling this method disables the delivery of visit-related events for your app. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Running the visits location service
- [func startMonitoringVisits()](./startmonitoringvisits%28%29.md)
  Starts the delivery of visit-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/stopmonitoringvisits())*