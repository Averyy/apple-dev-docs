# selfTestRequest(completion:)

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
func selfTestRequest(completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func selfTestRequest() async throws
```

```objc
- (void) selfTestRequestWithCompletion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustersmokecoalarm/selftestrequest(completion:))*