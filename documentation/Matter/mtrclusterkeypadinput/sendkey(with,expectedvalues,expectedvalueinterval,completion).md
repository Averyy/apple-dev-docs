# sendKey(with:expectedValues:expectedValueInterval:completion:)

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
func sendKey(with params: MTRKeypadInputClusterSendKeyParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRKeypadInputClusterSendKeyResponseParams?, (any Error)?) -> Void)
```

```swift
func sendKey(with params: MTRKeypadInputClusterSendKeyParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRKeypadInputClusterSendKeyResponseParams
```

```objc
- (void) sendKeyWithParams:(MTRKeypadInputClusterSendKeyParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRKeypadInputClusterSendKeyResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterkeypadinput/sendkey(with:expectedvalues:expectedvalueinterval:completion:))*