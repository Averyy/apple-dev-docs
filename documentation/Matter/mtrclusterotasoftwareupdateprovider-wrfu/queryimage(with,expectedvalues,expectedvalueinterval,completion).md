# queryImage(with:expectedValues:expectedValueInterval:completion:)

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
func queryImage(with params: MTROTASoftwareUpdateProviderClusterQueryImageParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTROTASoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)
```

```swift
func queryImage(with params: MTROTASoftwareUpdateProviderClusterQueryImageParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTROTASoftwareUpdateProviderClusterQueryImageResponseParams
```

```objc
- (void) queryImageWithParams:(MTROTASoftwareUpdateProviderClusterQueryImageParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTROTASoftwareUpdateProviderClusterQueryImageResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterotasoftwareupdateprovider-wrfu/queryimage(with:expectedvalues:expectedvalueinterval:completion:))*