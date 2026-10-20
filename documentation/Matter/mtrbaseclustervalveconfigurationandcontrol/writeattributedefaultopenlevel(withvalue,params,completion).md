# writeAttributeDefaultOpenLevel(withValue:params:completion:)

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
func writeAttributeDefaultOpenLevel(withValue value: NSNumber, params: MTRWriteParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeAttributeDefaultOpenLevel(withValue value: NSNumber, params: MTRWriteParams?) async throws
```

```objc
- (void) writeAttributeDefaultOpenLevelWithValue:(NSNumber *) value params:(MTRWriteParams *) params completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustervalveconfigurationandcontrol/writeattributedefaultopenlevel(withvalue:params:completion:))*