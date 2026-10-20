# readAttributeApplication(completion:)

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
func readAttributeApplication(completion: @escaping @Sendable (MTRApplicationBasicClusterApplicationStruct?, (any Error)?) -> Void)
```

```swift
func readAttributeApplication() async throws -> MTRApplicationBasicClusterApplicationStruct
```

```objc
- (void) readAttributeApplicationWithCompletion:(void (^)(MTRApplicationBasicClusterApplicationStruct *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterapplicationbasic/readattributeapplication(completion:))*