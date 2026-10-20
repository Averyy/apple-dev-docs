# readAttributeExpiryDate(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
func readAttributeExpiryDate(completion: @escaping @Sendable (NSNumber?, (any Error)?) -> Void)
```

```swift
func readAttributeExpiryDate() async throws -> NSNumber
```

```objc
- (void) readAttributeExpiryDateWithCompletion:(void (^)(NSNumber *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustersmokecoalarm/readattributeexpirydate(completion:))*