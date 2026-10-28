# identifiers

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A list of unique identifiers corresponding to detected feature points.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```objc
@property (nonatomic, readonly) const uint64_t * identifiers;
```

## Discussion

Each identifier in this list corresponds to the point vector at the same index in the [`points`](./points-7mppp.md) array.

## See Also

### Identifying Feature Points
- [count](./count.md)
  The number of points in the point cloud.
- [points](./points-7mppp.md)
  The list of detected points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arpointcloud/identifiers-7p42c)*