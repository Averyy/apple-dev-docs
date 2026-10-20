# requestContentsAuthorization(completion:)

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
func requestContentsAuthorization(completion: @escaping @Sendable (ICAuthorizationStatus) -> Void)
```

```swift
func requestContentsAuthorization() async -> ICAuthorizationStatus
```

```objc
- (void) requestContentsAuthorizationWithCompletion:(void (^)(ICAuthorizationStatus status)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/requestcontentsauthorization(completion:))*