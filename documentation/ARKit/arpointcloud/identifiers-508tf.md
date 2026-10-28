# identifiers

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A list of unique identifiers corresponding to detected feature points.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
@nonobjc
var identifiers: [UInt64] { get }
```

## Discussion

Each identifier in this list corresponds to the point vector at the same index in the [`points`](./points-4vkif.md) array.

## See Also

### Identifying Feature Points
- [var points: [simd_float3]](./points-4vkif.md)
  The list of detected points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arpointcloud/identifiers-508tf)*