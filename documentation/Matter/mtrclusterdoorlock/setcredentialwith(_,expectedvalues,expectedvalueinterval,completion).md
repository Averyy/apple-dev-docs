# setCredentialWith(_:expectedValues:expectedValueInterval:completion:)

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
func setCredentialWith(_ params: MTRDoorLockClusterSetCredentialParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRDoorLockClusterSetCredentialResponseParams?, (any Error)?) -> Void)
```

```swift
func setCredentialWith(_ params: MTRDoorLockClusterSetCredentialParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRDoorLockClusterSetCredentialResponseParams
```

```objc
- (void) setCredentialWithParams:(MTRDoorLockClusterSetCredentialParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRDoorLockClusterSetCredentialResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdoorlock/setcredentialwith(_:expectedvalues:expectedvalueinterval:completion:))*