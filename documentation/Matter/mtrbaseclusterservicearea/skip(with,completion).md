# skip(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SkipArea

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
func skip(with params: MTRServiceAreaClusterSkipAreaParams, completion: @escaping @Sendable (MTRServiceAreaClusterSkipAreaResponseParams?, (any Error)?) -> Void)
```

```swift
func skip(with params: MTRServiceAreaClusterSkipAreaParams) async throws -> MTRServiceAreaClusterSkipAreaResponseParams
```

```objc
- (void) skipAreaWithParams:(MTRServiceAreaClusterSkipAreaParams *) params completion:(void (^)(MTRServiceAreaClusterSkipAreaResponseParams *data, NSError *error)) completion;
```

## Discussion

This command is used to skip the given area, and to attempt operating at other areas on the SupportedAreas attribute list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterservicearea/skip(with:completion:))*