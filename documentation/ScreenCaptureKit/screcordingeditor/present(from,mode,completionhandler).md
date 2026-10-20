# present(from:mode:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- tvOS 27.0+

## Declaration

```swift
func present(from windowScene: UIWindowScene, mode: SCRecordingEditor.Mode, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func present(from windowScene: UIWindowScene, mode: SCRecordingEditor.Mode) async throws
```

```objc
- (void) presentFromWindowScene:(UIWindowScene *) windowScene mode:(SCRecordingEditorMode) mode completionHandler:(void (^)(NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/screcordingeditor/present(from:mode:completionhandler:))*