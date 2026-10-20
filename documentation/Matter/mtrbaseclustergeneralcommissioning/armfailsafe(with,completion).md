# armFailSafe(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func armFailSafe(with params: MTRGeneralCommissioningClusterArmFailSafeParams, completion: @escaping @Sendable (MTRGeneralCommissioningClusterArmFailSafeResponseParams?, (any Error)?) -> Void)
```

```swift
func armFailSafe(with params: MTRGeneralCommissioningClusterArmFailSafeParams) async throws -> MTRGeneralCommissioningClusterArmFailSafeResponseParams
```

```objc
- (void) armFailSafeWithParams:(MTRGeneralCommissioningClusterArmFailSafeParams *) params completion:(void (^)(MTRGeneralCommissioningClusterArmFailSafeResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergeneralcommissioning/armfailsafe(with:completion:))*