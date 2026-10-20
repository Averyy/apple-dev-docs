# ARAppClipCodeAnchor.URLDecodingState.decoding

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

A state that indicates the continuing process of decoding an App Clip Code’s URL.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+

## Declaration

```swift
case decoding
```

```c
ARAppClipCodeURLDecodingStateDecoding
```

#### Discussion

The App Clip Code anchor’s [`url`](../url.md) is `nil` in this state.

## See Also

### States
- [ARAppClipCodeAnchor.URLDecodingState.decoded](./decoded.md)
  A state that indicates the completed decoding of an App Clip Code URL.
- [ARAppClipCodeAnchor.URLDecodingState.failed](./failed.md)
  A state that indicates the failure to decode an App Clip Code’s URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arappclipcodeanchor/urldecodingstate-swift.enum/decoding)*