# selectionContainerViewBelowText

**Framework**: BrowserEngineKit  
**Kind**: property

If different than the text input view, one can return a container view here for selection views that draw  text. Includes the selection highlight view. If this is unimplemented or nil is returned, views are to be installed onto the text input view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
optional var selectionContainerViewBelowText: UIView? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/selectioncontainerviewbelowtext)*