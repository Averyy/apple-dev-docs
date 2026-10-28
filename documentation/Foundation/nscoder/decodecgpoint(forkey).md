# decodeCGPoint(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes and returns the Core Graphics point structure associated with the specified key in the coder’s archive.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func decodeCGPoint(forKey key: String) -> CGPoint
```

```objc
- (CGPoint) decodeCGPointForKey:(NSString *) key;
```

## Return Value

The `CGPoint` structure.

## Discussion

Use this method to decode a point that was previously encoded using the [`encode(_:forKey:)`](./encode%28_,forkey%29-7z9kc.md) method.

## Parameters

- `key`: The key that identifies the point.

## See Also

### Related Documentation
- [func encode(CGPoint, forKey: String)](./encode%28_,forkey%29-7z9kc.md)
  Encodes a point and associates it with the specified key in the receiver’s archive.
### Decoding Geometry-Based Data
- [func decodeCGAffineTransform(forKey: String) -> CGAffineTransform](./decodecgaffinetransform%28forkey%29.md)
  Decodes and returns the Core Graphics affine transform structure associated with the specified key in the coder’s archive.
- [func decodeCGRect(forKey: String) -> CGRect](./decodecgrect%28forkey%29.md)
  Decodes and returns the Core Graphics rectangle structure associated with the specified key in the coder’s archive.
- [func decodeCGSize(forKey: String) -> CGSize](./decodecgsize%28forkey%29.md)
  Decodes and returns the Core Graphics size structure associated with the specified key in the coder’s archive.
- [func decodeCGVector(forKey: String) -> CGVector](./decodecgvector%28forkey%29.md)
  Decodes and returns the Core Graphics vector data associated with the specified key in the coder’s archive.
- [func decodeDirectionalEdgeInsets(forKey: String) -> NSDirectionalEdgeInsets](./decodedirectionaledgeinsets%28forkey%29.md)
  Decodes and returns the UIKit directional edge insets structure associated with the specified key in the coder’s archive.
- [func decodeUIEdgeInsets(forKey: String) -> UIEdgeInsets](./decodeuiedgeinsets%28forkey%29.md)
  Decodes and returns the UIKit edge insets structure associated with the specified key in the coder’s archive.
- [func decodeUIOffset(forKey: String) -> UIOffset](./decodeuioffset%28forkey%29.md)
  Decodes and returns the UIKit offset structure associated with the specified key in the coder’s archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodecgpoint(forkey:))*