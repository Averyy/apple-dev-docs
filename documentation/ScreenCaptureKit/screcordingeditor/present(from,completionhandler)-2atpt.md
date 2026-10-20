# present(from:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func present(from windowScene: UIWindowScene, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func present(from windowScene: UIWindowScene) async throws
```

```objc
- (void) presentFromWindowScene:(UIWindowScene *) windowScene completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

Present the recording editor from the specified window scene.

## Parameters

- `windowScene`: The window scene to present from.
- `completionHandler`: Called when presentation completes. error is nil on success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/screcordingeditor/present(from:completionhandler:)-2atpt)*