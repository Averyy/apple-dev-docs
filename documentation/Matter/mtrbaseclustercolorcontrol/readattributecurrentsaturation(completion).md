# readAttributeCurrentSaturation(completion:)

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
func readAttributeCurrentSaturation(completion: @escaping @Sendable (NSNumber?, (any Error)?) -> Void)
```

```swift
func readAttributeCurrentSaturation() async throws -> NSNumber
```

```objc
- (void) readAttributeCurrentSaturationWithCompletion:(void (^)(NSNumber *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercolorcontrol/readattributecurrentsaturation(completion:))*