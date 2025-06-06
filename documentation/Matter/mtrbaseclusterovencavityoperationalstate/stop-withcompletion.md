# stop(with:completion:)

**Framework**: Matter  
**Kind**: method

Command Stop

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func stop(with params: MTROvenCavityOperationalStateClusterStopParams?) async throws -> MTROvenCavityOperationalStateClusterOperationalCommandResponseParams
```

#### Discussion

Upon receipt, the device SHALL stop its operation if it is at a position where it is safe to do so and/or permitted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterovencavityoperationalstate/stop(with:completion:))*