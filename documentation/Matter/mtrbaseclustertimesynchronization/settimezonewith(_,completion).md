# setTimeZoneWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetTimeZone

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
func setTimeZoneWith(_ params: MTRTimeSynchronizationClusterSetTimeZoneParams, completion: @escaping @Sendable (MTRTimeSynchronizationClusterSetTimeZoneResponseParams?, (any Error)?) -> Void)
```

```swift
func setTimeZoneWith(_ params: MTRTimeSynchronizationClusterSetTimeZoneParams) async throws -> MTRTimeSynchronizationClusterSetTimeZoneResponseParams
```

```objc
- (void) setTimeZoneWithParams:(MTRTimeSynchronizationClusterSetTimeZoneParams *) params completion:(void (^)(MTRTimeSynchronizationClusterSetTimeZoneResponseParams *data, NSError *error)) completion;
```

## Discussion

This command is used to set the time zone of the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization/settimezonewith(_:completion:))*