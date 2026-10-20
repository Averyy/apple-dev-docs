# remove(_:willInsertText:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes a placeholder object from the text input view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func remove(_ placeholder: UITextPlaceholder, willInsertText: Bool, completionHandler: @escaping @Sendable () -> Void)
```

```swift
func remove(_ placeholder: UITextPlaceholder, willInsertText: Bool) async
```

```objc
- (void) removeTextPlaceholder:(UITextPlaceholder *) placeholder willInsertText:(BOOL) willInsertText completionHandler:(void (^)()) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/remove(_:willinserttext:completionhandler:))*