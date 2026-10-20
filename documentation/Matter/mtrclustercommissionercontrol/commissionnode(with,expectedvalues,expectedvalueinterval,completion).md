# commissionNode(with:expectedValues:expectedValueInterval:completion:)

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
func commissionNode(with params: MTRCommissionerControlClusterCommissionNodeParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRCommissionerControlClusterReverseOpenCommissioningWindowParams?, (any Error)?) -> Void)
```

```swift
func commissionNode(with params: MTRCommissionerControlClusterCommissionNodeParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRCommissionerControlClusterReverseOpenCommissioningWindowParams
```

```objc
- (void) commissionNodeWithParams:(MTRCommissionerControlClusterCommissionNodeParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRCommissionerControlClusterReverseOpenCommissioningWindowParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustercommissionercontrol/commissionnode(with:expectedvalues:expectedvalueinterval:completion:))*