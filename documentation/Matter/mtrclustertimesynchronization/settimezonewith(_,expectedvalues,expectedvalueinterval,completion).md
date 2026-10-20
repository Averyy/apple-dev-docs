# setTimeZoneWith(_:expectedValues:expectedValueInterval:completion:)

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
func setTimeZoneWith(_ params: MTRTimeSynchronizationClusterSetTimeZoneParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRTimeSynchronizationClusterSetTimeZoneResponseParams?, (any Error)?) -> Void)
```

```swift
func setTimeZoneWith(_ params: MTRTimeSynchronizationClusterSetTimeZoneParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRTimeSynchronizationClusterSetTimeZoneResponseParams
```

```objc
- (void) setTimeZoneWithParams:(MTRTimeSynchronizationClusterSetTimeZoneParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRTimeSynchronizationClusterSetTimeZoneResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertimesynchronization/settimezonewith(_:expectedvalues:expectedvalueinterval:completion:))*