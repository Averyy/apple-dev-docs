# encode(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Encodes size information and associates it with the specified key in the coder’s archive.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func encode(_ size: CGSize, forKey key: String)
```

#### Discussion

When decoding the data from the archive, you pass the value in the `key` parameter to the corresponding [`decodeCGSize(forKey:)`](nscoder/decodecgsize(forkey:).md) method to retrieve the data.

## Parameters

- `size`: The size information to encode.
- `key`: The key identifying the data.

## See Also

- [func decodeCGSize(forKey: String) -> CGSize](nscoder/decodecgsize(forkey:).md)
  Decodes and returns the Core Graphics size structure associated with the specified key in the coder’s archive.
- [func encode(CGAffineTransform, forKey: String)](nscoder/encode(_:forkey:)-29jyx.md)
  Encodes an affine transform and associates it with the specified key in the receiver’s archive.
- [func encode(CGPoint, forKey: String)](nscoder/encode(_:forkey:)-7z9kc.md)
  Encodes a point and associates it with the specified key in the receiver’s archive.
- [func encode(CGRect, forKey: String)](nscoder/encode(_:forkey:)-10qhm.md)
  Encodes a rectangle and associates it with the specified key in the receiver’s archive.
- [func encode(CGVector, forKey: String)](nscoder/encode(_:forkey:)-26fxa.md)
  Encodes vector data and associates it with the specified key in the coder’s archive.
- [func encode(NSDirectionalEdgeInsets, forKey: String)](nscoder/encode(_:forkey:)-7oo2n.md)
  Encodes directional edge inset data and associates it with the specified key in the coder’s archive.
- [func encode(UIEdgeInsets, forKey: String)](nscoder/encode(_:forkey:)-44zsc.md)
  Encodes edge inset data and associates it with the specified key in the coder’s archive.
- [func encode(UIOffset, forKey: String)](nscoder/encode(_:forkey:)-9d1qy.md)
  Encodes offset data and associates it with the specified key in the coder’s archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-6wq3n)*