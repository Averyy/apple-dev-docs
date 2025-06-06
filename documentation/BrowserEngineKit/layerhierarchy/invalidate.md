# invalidate()

**Framework**: BrowserEngineKit  
**Kind**: method

Invalidates a layer hierarchy.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
func invalidate()
```

## Mentions

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)

#### Overview

When you call this method, the layer hierarchy can’t be hosted in a [`LayerHierarchyHostingView`](layerhierarchyhostingview.md). Communicate with the browser app to remove the hosting view from its superview.

## See Also

- [init() throws](layerhierarchy/init.md)
  Initializes a layer hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchy/invalidate())*