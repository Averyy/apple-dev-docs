# remove(_:willInsertText:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Removes a placeholder object from the text input view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func remove(_ placeholder: UITextPlaceholder, willInsertText: Bool) async
```

## See Also

- [func insertTextPlaceholder(size: CGSize, completionHandler: (UITextPlaceholder) -> Void)](betextinput/inserttextplaceholder(size:completionhandler:).md)
  Inserts a placeholder object to reserve visual space during text input. If `size.height` is less than or equal to zero, then the placeholder is inline and line height. If `size.height` is greather than zero, then the placeholder is treated as a paragraph of height `size.height`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/remove(_:willinserttext:completionhandler:))*