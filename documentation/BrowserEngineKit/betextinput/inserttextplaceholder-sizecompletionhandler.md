# insertTextPlaceholder(size:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Inserts a placeholder object to reserve visual space during text input. If `size.height` is less than or equal to zero, then the placeholder is inline and line height. If `size.height` is greather than zero, then the placeholder is treated as a paragraph of height `size.height`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func insertTextPlaceholder(size: CGSize) async -> UITextPlaceholder
```

## See Also

- [func remove(UITextPlaceholder, willInsertText: Bool, completionHandler: () -> Void)](betextinput/remove(_:willinserttext:completionhandler:).md)
  Removes a placeholder object from the text input view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/inserttextplaceholder(size:completionhandler:))*