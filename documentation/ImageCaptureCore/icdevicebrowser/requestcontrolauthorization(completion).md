# requestControlAuthorization(completion:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func requestControlAuthorization(completion: @escaping @Sendable (ICAuthorizationStatus) -> Void)
```

```swift
func requestControlAuthorization() async -> ICAuthorizationStatus
```

```objc
- (void) requestControlAuthorizationWithCompletion:(void (^)(ICAuthorizationStatus status)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/requestcontrolauthorization(completion:))*