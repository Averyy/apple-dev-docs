# stopMonitoringSignificantLocationChanges()

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Stops the delivery of location events based on significant location changes.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func stopMonitoringSignificantLocationChanges()
```

```objc
- (void) stopMonitoringSignificantLocationChanges;
```

## Discussion

Use this method to stop the delivery of location events that was started using the [`startMonitoringSignificantLocationChanges()`](./startmonitoringsignificantlocationchanges%28%29.md) method. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

### Running the significant change location service
- [func startMonitoringSignificantLocationChanges()](./startmonitoringsignificantlocationchanges%28%29.md)
  Starts the generation of updates based on significant location changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/stopmonitoringsignificantlocationchanges())*