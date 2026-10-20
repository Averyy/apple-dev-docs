# resumeRequest(completion:)

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
func resumeRequest(completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func resumeRequest() async throws
```

```objc
- (void) resumeRequestWithCompletion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement/resumerequest(completion:))*