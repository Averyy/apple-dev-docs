# writeAttributeColorPointGX(withValue:params:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+ - Deprecated in 26.1
- iPadOS 16.4+ - Deprecated in 26.1
- Mac Catalyst 16.4+ - Deprecated in 26.1
- macOS 13.3+ - Deprecated in 26.1
- tvOS 16.4+ - Deprecated in 26.1
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 9.4+ - Deprecated in 26.1

> **Deprecated**: This attribute is no longer writable in the Matter standard

## Declaration

```swift
func writeAttributeColorPointGX(withValue value: NSNumber, params: MTRWriteParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeAttributeColorPointGX(withValue value: NSNumber, params: MTRWriteParams?) async throws
```

```objc
- (void) writeAttributeColorPointGXWithValue:(NSNumber *) value params:(MTRWriteParams *) params completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercolorcontrol/writeattributecolorpointgx(withvalue:params:completion:))*