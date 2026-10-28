# ARAppClipCodeAnchor.URLDecodingState

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The states in the process of decoding an App Clip code URL.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+

## Declaration

```swift
enum URLDecodingState
```

```c
enum ARAppClipCodeURLDecodingState : NSInteger;
```

## Overview

The possible states of decoding the [`url`](./url.md) of an App Clip Code.

## Topics

### States
- [ARAppClipCodeAnchor.URLDecodingState.decoded](./urldecodingstate-swift.enum/decoded.md)
  A state that indicates the completed decoding of an App Clip Code URL.
- [ARAppClipCodeAnchor.URLDecodingState.decoding](./urldecodingstate-swift.enum/decoding.md)
  A state that indicates the continuing process of decoding an App Clip Code’s URL.
- [ARAppClipCodeAnchor.URLDecodingState.failed](./urldecodingstate-swift.enum/failed.md)
  A state that indicates the failure to decode an App Clip Code’s URL.
### Initializers
- [init?(rawValue: Int)](./urldecodingstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Decoding the URL
- [var url: URL?](./url.md)
  The URL encoded in an App Clip Code.
- [var urlDecodingState: ARAppClipCodeAnchor.URLDecodingState](./urldecodingstate-swift.property.md)
  A state that indicates the process of decoding an App Clip Code URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arappclipcodeanchor/urldecodingstate-swift.enum)*