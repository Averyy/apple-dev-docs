# layer

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

The layer represented by this layer hierarchy.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
var layer: CALayer? { get set }
```

```objc
@property (nonatomic, strong, nullable) CALayer * layer;
```

#### Discussion

Set this property to the root layer of the hierarchy that you host in a [`LayerHierarchyHostingView`](../layerhierarchyhostingview.md) in the browser app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchy/layer)*