# type

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The kind of detected feature the search result represents.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use raycasting

## Declaration

```swift
var type: ARHitTestResult.ResultType { get }
```

```objc
@property (nonatomic, readonly) ARHitTestResultType type;
```

## Discussion

You specify one or more result types to search for when calling a hit-testing method. A result object has only one result type.

## See Also

### Identifying Results
- [ARHitTestResult.ResultType](./resulttype.md)
  Possible types for specifying a hit-test search, or for the result of a hit-test search.
- [var anchor: ARAnchor?](./anchor.md)
  The anchor representing the detected surface, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/type)*