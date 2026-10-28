# setTrustedTimeSourceWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetTrustedTimeSource

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
func setTrustedTimeSourceWith(_ params: MTRTimeSynchronizationClusterSetTrustedTimeSourceParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setTrustedTimeSourceWith(_ params: MTRTimeSynchronizationClusterSetTrustedTimeSourceParams) async throws
```

```objc
- (void) setTrustedTimeSourceWithParams:(MTRTimeSynchronizationClusterSetTrustedTimeSourceParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

This command is used to set the TrustedTimeSource attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization/settrustedtimesourcewith(_:completion:))*