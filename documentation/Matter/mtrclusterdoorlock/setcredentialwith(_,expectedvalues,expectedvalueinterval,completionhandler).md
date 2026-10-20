# setCredentialWith(_:expectedValues:expectedValueInterval:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use setCredentialWithParams:expectedValues:expectedValueInterval:completion:

## Declaration

```swift
func setCredentialWith(_ params: MTRDoorLockClusterSetCredentialParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completionHandler: @escaping @Sendable (MTRDoorLockClusterSetCredentialResponseParams?, (any Error)?) -> Void)
```

```swift
func setCredentialWith(_ params: MTRDoorLockClusterSetCredentialParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRDoorLockClusterSetCredentialResponseParams
```

```objc
- (void) setCredentialWithParams:(MTRDoorLockClusterSetCredentialParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completionHandler:(void (^)(MTRDoorLockClusterSetCredentialResponseParams *data, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdoorlock/setcredentialwith(_:expectedvalues:expectedvalueinterval:completionhandler:))*