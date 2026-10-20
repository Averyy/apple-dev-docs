# queryImage(with:completion:)

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
func queryImage(with params: MTROTASoftwareUpdateProviderClusterQueryImageParams, completion: @escaping @Sendable (MTROTASoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)
```

```swift
func queryImage(with params: MTROTASoftwareUpdateProviderClusterQueryImageParams) async throws -> MTROTASoftwareUpdateProviderClusterQueryImageResponseParams
```

```objc
- (void) queryImageWithParams:(MTROTASoftwareUpdateProviderClusterQueryImageParams *) params completion:(void (^)(MTROTASoftwareUpdateProviderClusterQueryImageResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterotasoftwareupdateprovider-8bnit/queryimage(with:completion:))*