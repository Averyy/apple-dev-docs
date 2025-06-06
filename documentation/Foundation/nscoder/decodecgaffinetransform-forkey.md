# decodeCGAffineTransform(forKey:)

**Framework**: Foundation  
**Kind**: method

Decodes and returns the Core Graphics affine transform structure associated with the specified key in the coder’s archive.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func decodeCGAffineTransform(forKey key: String) -> CGAffineTransform
```

#### Return Value

The affine transform.

#### Discussion

Use this method to decode size information that was previously encoded using the [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-29jyx.md) method.

## Parameters

- `key`: The key that identifies the affine transform.

## See Also

- [func encode(CGAffineTransform, forKey: String)](nscoder/encode(_:forkey:)-29jyx.md)
  Encodes an affine transform and associates it with the specified key in the receiver’s archive.
- [func decodeCGPoint(forKey: String) -> CGPoint](nscoder/decodecgpoint(forkey:).md)
  Decodes and returns the Core Graphics point structure associated with the specified key in the coder’s archive.
- [func decodeCGRect(forKey: String) -> CGRect](nscoder/decodecgrect(forkey:).md)
  Decodes and returns the Core Graphics rectangle structure associated with the specified key in the coder’s archive.
- [func decodeCGSize(forKey: String) -> CGSize](nscoder/decodecgsize(forkey:).md)
  Decodes and returns the Core Graphics size structure associated with the specified key in the coder’s archive.
- [func decodeCGVector(forKey: String) -> CGVector](nscoder/decodecgvector(forkey:).md)
  Decodes and returns the Core Graphics vector data associated with the specified key in the coder’s archive.
- [func decodeDirectionalEdgeInsets(forKey: String) -> NSDirectionalEdgeInsets](nscoder/decodedirectionaledgeinsets(forkey:).md)
  Decodes and returns the UIKit directional edge insets structure associated with the specified key in the coder’s archive.
- [func decodeUIEdgeInsets(forKey: String) -> UIEdgeInsets](nscoder/decodeuiedgeinsets(forkey:).md)
  Decodes and returns the UIKit edge insets structure associated with the specified key in the coder’s archive.
- [func decodeUIOffset(forKey: String) -> UIOffset](nscoder/decodeuioffset(forkey:).md)
  Decodes and returns the UIKit offset structure associated with the specified key in the coder’s archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodecgaffinetransform(forkey:))*