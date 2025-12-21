# selectionContainerViewAboveText

**Framework**: BrowserEngineKit  
**Kind**: property

If different than the text input view, one can return a container view here for selection views that draw  text. Includes selection range adjustment handles. If this is unimplemented or nil is returned, views are to be installed onto the text input view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
optional var selectionContainerViewAboveText: UIView? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/selectioncontainerviewabovetext)*