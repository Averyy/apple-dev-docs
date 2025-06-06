# createVisibilityPropagationInteraction()

**Framework**: BrowserEngineKit  
**Kind**: method

Returns an interaction that associates a view with the rendering process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
func createVisibilityPropagationInteraction() -> any UIInteraction
```

#### Overview

When you add a visibility propagation interaction to a view, the operating system treats the extension process as “visible” whenever the view is visible, and schedules the process as if it has visible UI. When the view is not visible, the operating system schedules the process as a background helper.

If your rendering extension prepares content for multiple views, create a separate visibility propagation for each view.

## See Also

- [Propagating view visibility information to extension processes](propagating-view-visibility-information-to-browser-extensions.md)
  Register the extensions that contribute to preparing your browser app’s UI.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](webcontentprocess/createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the web content process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingprocess/createvisibilitypropagationinteraction())*