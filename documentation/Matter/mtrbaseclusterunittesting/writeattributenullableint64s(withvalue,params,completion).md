# writeAttributeNullableInt64s(withValue:params:completion:)

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
func writeAttributeNullableInt64s(withValue value: NSNumber?, params: MTRWriteParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeAttributeNullableInt64s(withValue value: NSNumber?, params: MTRWriteParams?) async throws
```

```objc
- (void) writeAttributeNullableInt64sWithValue:(NSNumber *) value params:(MTRWriteParams *) params completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterunittesting/writeattributenullableint64s(withvalue:params:completion:))*