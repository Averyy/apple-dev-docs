# readAttributeOperationalError(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func readAttributeOperationalError(completion: @escaping @Sendable (MTROperationalStateClusterErrorStateStruct?, (any Error)?) -> Void)
```

```swift
func readAttributeOperationalError() async throws -> MTROperationalStateClusterErrorStateStruct
```

```objc
- (void) readAttributeOperationalErrorWithCompletion:(void (^)(MTROperationalStateClusterErrorStateStruct *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalstate/readattributeoperationalerror(completion:))*