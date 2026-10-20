# timeSnapshot(with:expectedValues:expectedValueInterval:completion:)

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
func timeSnapshot(with params: MTRGeneralDiagnosticsClusterTimeSnapshotParams?, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams?, (any Error)?) -> Void)
```

```swift
func timeSnapshot(with params: MTRGeneralDiagnosticsClusterTimeSnapshotParams?, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams
```

```objc
- (void) timeSnapshotWithParams:(MTRGeneralDiagnosticsClusterTimeSnapshotParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergeneraldiagnostics/timesnapshot(with:expectedvalues:expectedvalueinterval:completion:))*