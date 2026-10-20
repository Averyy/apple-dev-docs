# invalidate()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Invalidates a layer hierarchy.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func invalidate()
```

```objc
- (void) invalidate;
```

## Mentions

- [Hosting browser view layers in the rendering extension](../hosting-browser-view-layers-in-the-rendering-extension.md)

#### Discussion

When you call this method, the layer hierarchy is no longer of use. Communicate with your browser app process to remove the related hosting view ([`LayerHierarchyHostingView`](../layerhierarchyhostingview.md)) from its superview.

## See Also

### Creating and invalidating a layer hierarchy
- [init() throws](./init%28%29.md)
  Initializes a layer hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchy/invalidate())*