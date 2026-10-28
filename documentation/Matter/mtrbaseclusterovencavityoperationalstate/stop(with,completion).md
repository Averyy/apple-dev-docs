# stop(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func stop(with params: MTROvenCavityOperationalStateClusterStopParams?, completion: @escaping @Sendable (MTROvenCavityOperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)
```

```swift
func stop(with params: MTROvenCavityOperationalStateClusterStopParams?) async throws -> MTROvenCavityOperationalStateClusterOperationalCommandResponseParams
```

```objc
- (void) stopWithParams:(MTROvenCavityOperationalStateClusterStopParams *) params completion:(void (^)(MTROvenCavityOperationalStateClusterOperationalCommandResponseParams *data, NSError *error)) completion;
```

## Discussion

This command SHALL be supported if the device supports remotely stopping the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterovencavityoperationalstate/stop(with:completion:))*