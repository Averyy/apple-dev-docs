# readAttributeDefaultOTAProviders(with:completion:)

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
func readAttributeDefaultOTAProviders(with params: MTRReadParams?, completion: @escaping @Sendable ([Any]?, (any Error)?) -> Void)
```

```swift
func readAttributeDefaultOTAProviders(with params: MTRReadParams?) async throws -> [Any]
```

```objc
- (void) readAttributeDefaultOTAProvidersWithParams:(MTRReadParams *) params completion:(void (^)(NSArray *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterotasoftwareupdaterequestor-9n6nb/readattributedefaultotaproviders(with:completion:))*