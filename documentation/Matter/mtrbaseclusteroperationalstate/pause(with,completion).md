# pause(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func pause(with params: MTROperationalStateClusterPauseParams?, completion: @escaping @Sendable (MTROperationalStateClusterOperationalCommandResponseParams?, (any Error)?) -> Void)
```

```swift
func pause(with params: MTROperationalStateClusterPauseParams?) async throws -> MTROperationalStateClusterOperationalCommandResponseParams
```

```objc
- (void) pauseWithParams:(MTROperationalStateClusterPauseParams *) params completion:(void (^)(MTROperationalStateClusterOperationalCommandResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalstate/pause(with:completion:))*