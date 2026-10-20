# resetContentsAuthorization(completion:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
func resetContentsAuthorization(completion: @escaping @Sendable (ICAuthorizationStatus) -> Void)
```

```swift
func resetContentsAuthorization() async -> ICAuthorizationStatus
```

```objc
- (void) resetContentsAuthorizationWithCompletion:(void (^)(ICAuthorizationStatus status)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/resetcontentsauthorization(completion:))*