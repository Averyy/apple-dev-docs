# readAttributeMinFrequency(completion:)

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
func readAttributeMinFrequency(completion: @escaping @Sendable (NSNumber?, (any Error)?) -> Void)
```

```swift
func readAttributeMinFrequency() async throws -> NSNumber
```

```objc
- (void) readAttributeMinFrequencyWithCompletion:(void (^)(NSNumber *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterlevelcontrol/readattributeminfrequency(completion:))*