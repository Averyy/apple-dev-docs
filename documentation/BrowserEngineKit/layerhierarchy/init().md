# init()

**Framework**: BrowserEngineKit  
**Kind**: init  
**Role**: Initializer

Initializes a layer hierarchy.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init() throws
```

```objc
+ (BELayerHierarchy *) layerHierarchyWithError:(NSError **) error;
```

## Discussion

This initializer can fail and throw an error if your extension can’t establish a connection to the rendering server.

## See Also

### Creating and invalidating a layer hierarchy
- [func invalidate()](./invalidate%28%29.md)
  Invalidates a layer hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchy/init())*