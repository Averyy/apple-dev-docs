# ARAppClipCodeAnchor.URLDecodingState

**Framework**: ARKit  
**Kind**: enum

The states in the process of decoding an App Clip code URL.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+

## Declaration

```swift
enum URLDecodingState
```

#### Overview

The possible states of decoding the [`url`](arappclipcodeanchor/url.md) of an App Clip Code.

## Topics

### States
- [ARAppClipCodeAnchor.URLDecodingState.decoded](arappclipcodeanchor/urldecodingstate-swift.enum/decoded.md)
  A state that indicates the completed decoding of an App Clip Code URL.
- [ARAppClipCodeAnchor.URLDecodingState.decoding](arappclipcodeanchor/urldecodingstate-swift.enum/decoding.md)
  A state that indicates the continuing process of decoding an App Clip Code’s URL.
- [ARAppClipCodeAnchor.URLDecodingState.failed](arappclipcodeanchor/urldecodingstate-swift.enum/failed.md)
  A state that indicates the failure to decode an App Clip Code’s URL.
### Initializers
- [init?(rawValue: Int)](arappclipcodeanchor/urldecodingstate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var url: URL?](arappclipcodeanchor/url.md)
  The URL encoded in an App Clip Code.
- [var urlDecodingState: ARAppClipCodeAnchor.URLDecodingState](arappclipcodeanchor/urldecodingstate-swift.property.md)
  A state that indicates the process of decoding an App Clip Code URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arappclipcodeanchor/urldecodingstate-swift.enum)*