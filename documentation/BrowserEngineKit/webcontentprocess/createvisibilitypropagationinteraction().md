# createVisibilityPropagationInteraction()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Returns an interaction that associates a view with the web content process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func createVisibilityPropagationInteraction() -> any UIInteraction
```

#### Discussion

When you add a visibility propagation interaction to a view, the system considers the extension process visible whenever the view is visible, and schedules the process as if it has visible UI. When the view is not visible, the system schedules the process as a background helper.

If your web content extension prepares content for multiple views, create a separate visibility propagation for each view.

## See Also

### Visibility propagation
- [Propagating view visibility information to extension processes](../propagating-view-visibility-information-to-browser-extensions.md)
  Register the extensions that contribute to preparing your browser app’s UI.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](../renderingprocess/createvisibilitypropagationinteraction%28%29.md)
  Returns an interaction that associates a view with the rendering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/webcontentprocess/createvisibilitypropagationinteraction())*