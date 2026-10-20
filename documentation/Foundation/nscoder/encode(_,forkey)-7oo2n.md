# encode(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Encodes directional edge inset data and associates it with the specified key in the coder’s archive.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func encode(_ insets: NSDirectionalEdgeInsets, forKey key: String)
```

```objc
- (void) encodeDirectionalEdgeInsets:(NSDirectionalEdgeInsets) insets forKey:(NSString *) key;
```

#### Discussion

When decoding the data from the archive, you pass the value in the key parameter to the corresponding [`decodeDirectionalEdgeInsets(forKey:)`](./decodedirectionaledgeinsets%28forkey%29.md) method to retrieve the data.

## Parameters

- `insets`: The edge insets data to encode.
- `key`: The key identifying the data.

## See Also

### Encoding Geometry-Based Data
- [func encode(CGAffineTransform, forKey: String)](./encode%28_,forkey%29-29jyx.md)
  Encodes an affine transform and associates it with the specified key in the receiver’s archive.
- [func encode(CGPoint, forKey: String)](./encode%28_,forkey%29-7z9kc.md)
  Encodes a point and associates it with the specified key in the receiver’s archive.
- [func encode(CGRect, forKey: String)](./encode%28_,forkey%29-10qhm.md)
  Encodes a rectangle and associates it with the specified key in the receiver’s archive.
- [func encode(CGSize, forKey: String)](./encode%28_,forkey%29-6wq3n.md)
  Encodes size information and associates it with the specified key in the coder’s archive.
- [func encode(CGVector, forKey: String)](./encode%28_,forkey%29-26fxa.md)
  Encodes vector data and associates it with the specified key in the coder’s archive.
- [func encode(UIEdgeInsets, forKey: String)](./encode%28_,forkey%29-44zsc.md)
  Encodes edge inset data and associates it with the specified key in the coder’s archive.
- [func encode(UIOffset, forKey: String)](./encode%28_,forkey%29-9d1qy.md)
  Encodes offset data and associates it with the specified key in the coder’s archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-7oo2n)*