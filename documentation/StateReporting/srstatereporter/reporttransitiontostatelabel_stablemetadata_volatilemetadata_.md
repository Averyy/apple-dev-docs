# reportTransitionToStateLabel:stableMetadata:volatileMetadata:

**Framework**: StateReporting  
**Kind**: method  
**Role**: Instance Method

Reports a transition to a new state.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```objc
- (void) reportTransitionToStateLabel:(NSString *) stateLabel stableMetadata:(NSDictionary<NSString *,NSObject *> *) stableMetadata volatileMetadata:(NSDictionary<NSString *,NSObject *> *) volatileMetadata;
```

## Discussion

A transition occurs only when `stateLabel` or `stableMetadata` changes from the current state. If both are equal to the current values, this call is a no-op. Pass `nil` for `stateLabel` to indicate that no state is currently active, clearing any previously reported state. Any volatile metadata from the previous state is discarded when a new transition begins. Calling this method more frequently than user interaction timescales can trigger rate limiting, causing state updates to go unlogged.

## Parameters

- `stateLabel`: A descriptive label for the new state, which must not be empty, or `nil` to clear the active state.
- `stableMetadata`: An optional dictionary with `NSString` keys that identifies the state together with `stateLabel`. Dictionary values must be `NSNumber`, `NSString`, or `NSDate`. Passing values of any other type is a programmer error and will raise an exception.
- `volatileMetadata`: An optional dictionary with `NSString` keys providing context likely to change within this state. Dictionary values must be `NSNumber`, `NSString`, or `NSDate`. Passing values of any other type is a programmer error and will raise an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/srstatereporter/reporttransitiontostatelabel:stablemetadata:volatilemetadata:)*