# requestPreferredArrowDirectionForEditMenu(completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invoked by the system to gather context, including the client’s preference for how the edit menu should be positioned relative to the selected text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func requestPreferredArrowDirectionForEditMenu(completionHandler: @escaping @Sendable (UIEditMenuArrowDirection) -> Void)
```

```swift
func requestPreferredArrowDirectionForEditMenu() async -> UIEditMenuArrowDirection
```

```objc
- (void) requestPreferredArrowDirectionForEditMenuWithCompletionHandler:(void (^)(UIEditMenuArrowDirection )) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/requestpreferredarrowdirectionforeditmenu(completionhandler:))*