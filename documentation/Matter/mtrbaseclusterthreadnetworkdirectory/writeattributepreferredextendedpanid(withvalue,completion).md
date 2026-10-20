# writeAttributePreferredExtendedPanID(withValue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func writeAttributePreferredExtendedPanID(withValue value: Data?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeAttributePreferredExtendedPanID(withValue value: Data?) async throws
```

```objc
- (void) writeAttributePreferredExtendedPanIDWithValue:(NSData *) value completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadnetworkdirectory/writeattributepreferredextendedpanid(withvalue:completion:))*