# setAliroReaderConfigWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetAliroReaderConfig

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
func setAliroReaderConfigWith(_ params: MTRDoorLockClusterSetAliroReaderConfigParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setAliroReaderConfigWith(_ params: MTRDoorLockClusterSetAliroReaderConfigParams) async throws
```

```objc
- (void) setAliroReaderConfigWithParams:(MTRDoorLockClusterSetAliroReaderConfigParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

This command allows communicating an Aliro Reader configuration, as defined in Aliro, to the lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdoorlock/setaliroreaderconfigwith(_:completion:))*