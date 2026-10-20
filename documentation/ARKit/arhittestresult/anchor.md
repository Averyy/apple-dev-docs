# anchor

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The anchor representing the detected surface, if any.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use raycasting

## Declaration

```swift
var anchor: ARAnchor? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) ARAnchor * anchor;
```

#### Discussion

Results of the [`featurePoint`](./resulttype/featurepoint.md) type do not include an anchor.

## See Also

### Identifying Results
- [var type: ARHitTestResult.ResultType](./type.md)
  The kind of detected feature the search result represents.
- [ARHitTestResult.ResultType](./resulttype.md)
  Possible types for specifying a hit-test search, or for the result of a hit-test search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/anchor)*