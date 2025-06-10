# ARAppClipCodeAnchor.URLDecodingState.failed

**Framework**: ARKit  
**Kind**: case

A state that indicates the failure to decode an App Clip Code’s URL.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+

## Declaration

```swift
case failed
```

#### Discussion

The decoding of an App Clip Code URL fails under these circumstances:

- The full app or App Clip is missing the associated-domains entitlement from its code signature.
- The host of the resource identified by the App Clip Code URL doesn’t vend an Apple App Site Association (AASA) file.
- The AASA file hosted at the App Clip Code URL’s domain lacks the App Clip’s fully-qualified application identifier.
- The App Clip Code is not associated to the App Clip in an App Clip experience in App Store Connect.

For more information, see [`Configuring App Clip experiences`](https://developer.apple.com/documentation/AppClip/configuring-the-launch-experience-of-your-app-clip).

## See Also

- [ARAppClipCodeAnchor.URLDecodingState.decoded](arappclipcodeanchor/urldecodingstate-swift.enum/decoded.md)
  A state that indicates the completed decoding of an App Clip Code URL.
- [ARAppClipCodeAnchor.URLDecodingState.decoding](arappclipcodeanchor/urldecodingstate-swift.enum/decoding.md)
  A state that indicates the continuing process of decoding an App Clip Code’s URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arappclipcodeanchor/urldecodingstate-swift.enum/failed)*