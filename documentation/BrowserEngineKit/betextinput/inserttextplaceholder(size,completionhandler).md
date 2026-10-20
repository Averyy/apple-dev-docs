# insertTextPlaceholder(size:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Inserts a placeholder object to reserve visual space during text input.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func insertTextPlaceholder(size: CGSize, completionHandler: @escaping @Sendable (UITextPlaceholder) -> Void)
```

```swift
func insertTextPlaceholder(size: CGSize) async -> UITextPlaceholder
```

```objc
- (void) insertTextPlaceholderWithSize:(CGSize) size completionHandler:(void (^)(UITextPlaceholder *)) completionHandler;
```

#### Discussion

If `size.height` is less than or equal to zero, then the placeholder is inline and line height. If `size.height` is greater than zero, then the placeholder is a paragraph of height `size.height`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/inserttextplaceholder(size:completionhandler:))*