# getTargetsWith(_:expectedValues:expectedValueInterval:completion:)

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
func getTargetsWith(_ params: MTREnergyEVSEClusterGetTargetsParams?, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)
```

```swift
func targets(with params: MTREnergyEVSEClusterGetTargetsParams?, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTREnergyEVSEClusterGetTargetsResponseParams
```

```objc
- (void) getTargetsWithParams:(MTREnergyEVSEClusterGetTargetsParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTREnergyEVSEClusterGetTargetsResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterenergyevse/gettargetswith(_:expectedvalues:expectedvalueinterval:completion:))*