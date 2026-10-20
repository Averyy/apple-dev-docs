# readAttributeProductName(completion:)

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
func readAttributeProductName(completion: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
func readAttributeProductName() async throws -> String
```

```objc
- (void) readAttributeProductNameWithCompletion:(void (^)(NSString *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasicinformation/readattributeproductname(completion:))*