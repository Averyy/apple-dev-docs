# readAttributeNOCs(with:completion:)

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
func readAttributeNOCs(with params: MTRReadParams?, completion: @escaping @Sendable ([Any]?, (any Error)?) -> Void)
```

```swift
func readAttributeNOCs(with params: MTRReadParams?) async throws -> [Any]
```

```objc
- (void) readAttributeNOCsWithParams:(MTRReadParams *) params completion:(void (^)(NSArray *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalcredentials/readattributenocs(with:completion:))*