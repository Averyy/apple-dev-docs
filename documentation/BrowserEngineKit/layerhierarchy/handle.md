# handle

**Framework**: BrowserEngineKit  
**Kind**: property

A reference to the layer hierarchy that you add to the hosting view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
var handle: LayerHierarchyHandle { get }
```

#### Discussion

Get the handle in your extension process, then use XPC to send it to the browser app. In the browser app, add the handle to a [`LayerHierarchyHostingView`](layerhierarchyhostingview.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchy/handle)*