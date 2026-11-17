# stateReason

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The reasons for the app’s geo tracking status.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
var stateReason: ARGeoTrackingStatus.StateReason { get }
```

```objc
@property (nonatomic, readonly) ARGeoTrackingStateReason stateReason;
```

## Discussion

These possible values provide more information about a geo tracking session’s current [`state`](./state-swift.property.md).

## See Also

### Determining the Reason
- [ARGeoTrackingStatus.StateReason](./statereason-swift.enum.md)
  The reasons that describe a geo tracking session’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingstatus/statereason-swift.property)*