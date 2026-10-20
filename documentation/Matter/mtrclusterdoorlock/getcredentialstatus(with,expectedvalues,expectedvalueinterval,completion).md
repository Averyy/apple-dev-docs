# getCredentialStatus(with:expectedValues:expectedValueInterval:completion:)

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
func getCredentialStatus(with params: MTRDoorLockClusterGetCredentialStatusParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRDoorLockClusterGetCredentialStatusResponseParams?, (any Error)?) -> Void)
```

```swift
func credentialStatus(with params: MTRDoorLockClusterGetCredentialStatusParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRDoorLockClusterGetCredentialStatusResponseParams
```

```objc
- (void) getCredentialStatusWithParams:(MTRDoorLockClusterGetCredentialStatusParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRDoorLockClusterGetCredentialStatusResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdoorlock/getcredentialstatus(with:expectedvalues:expectedvalueinterval:completion:))*