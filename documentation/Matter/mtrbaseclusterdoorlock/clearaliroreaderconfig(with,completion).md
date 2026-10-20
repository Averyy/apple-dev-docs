# clearAliroReaderConfig(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command ClearAliroReaderConfig

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
func clearAliroReaderConfig(with params: MTRDoorLockClusterClearAliroReaderConfigParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func clearAliroReaderConfig(with params: MTRDoorLockClusterClearAliroReaderConfigParams?) async throws
```

```objc
- (void) clearAliroReaderConfigWithParams:(MTRDoorLockClusterClearAliroReaderConfigParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command allows clearing an existing Aliro Reader configuration for the lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdoorlock/clearaliroreaderconfig(with:completion:))*