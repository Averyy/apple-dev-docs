# readAttributeTrustedTimeSource(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func readAttributeTrustedTimeSource(completion: @escaping @Sendable (MTRTimeSynchronizationClusterTrustedTimeSourceStruct?, (any Error)?) -> Void)
```

```swift
func readAttributeTrustedTimeSource() async throws -> MTRTimeSynchronizationClusterTrustedTimeSourceStruct
```

```objc
- (void) readAttributeTrustedTimeSourceWithCompletion:(void (^)(MTRTimeSynchronizationClusterTrustedTimeSourceStruct *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization/readattributetrustedtimesource(completion:))*