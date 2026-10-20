# writeAttributeLocation(withValue:completion:)

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
func writeAttributeLocation(withValue value: String, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeAttributeLocation(withValue value: String) async throws
```

```objc
- (void) writeAttributeLocationWithValue:(NSString *) value completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasicinformation/writeattributelocation(withvalue:completion:))*