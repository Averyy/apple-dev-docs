# getSetupPIN(with:completion:)

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
func getSetupPIN(with params: MTRAccountLoginClusterGetSetupPINParams, completion: @escaping @Sendable (MTRAccountLoginClusterGetSetupPINResponseParams?, (any Error)?) -> Void)
```

```swift
func setupPIN(with params: MTRAccountLoginClusterGetSetupPINParams) async throws -> MTRAccountLoginClusterGetSetupPINResponseParams
```

```objc
- (void) getSetupPINWithParams:(MTRAccountLoginClusterGetSetupPINParams *) params completion:(void (^)(MTRAccountLoginClusterGetSetupPINResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteraccountlogin/getsetuppin(with:completion:))*