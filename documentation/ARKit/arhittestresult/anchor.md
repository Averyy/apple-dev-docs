# anchor

**Framework**: ARKit  
**Kind**: property

The anchor representing the detected surface, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var anchor: ARAnchor? { get }
```

#### Discussion

Results of the [`featurePoint`](arhittestresult/resulttype/featurepoint.md) type do not include an anchor.

## See Also

- [var type: ARHitTestResult.ResultType](arhittestresult/type.md)
  The kind of detected feature the search result represents.
- [ARHitTestResult.ResultType](arhittestresult/resulttype.md)
  Possible types for specifying a hit-test search, or for the result of a hit-test search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/anchor)*