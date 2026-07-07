# supportsAdvisoryKeys

**Framework**: AVFoundation  
**Kind**: property

Boolean indicating whether advisory keys are enabled on the client.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var supportsAdvisoryKeys: Bool { get set }
```

#### Discussion

Set to true to enable advisory key loading. False by default. Note that this is a one-way operation—once set to true, this property cannot be set back to false.

Advisory key loading allows applications to make use of content keys provided speculatively by the key server. When enabled, FairPlay may cache these keys and return them immediately on subsequent requests without requiring a round-trip to the key server.

The delegate must be prepared to handle advisory key requests by checking the `canBeFulfilledWithAdvisoryKey` property on `AVContentKeyRequest` objects.

When an advisory key is already cached by FairPlay, `makeStreamingContentKeyRequestData` will return nil for the key request data, and `canBeFulfilledWithAdvisoryKey` will return true. In this case, no request to the key server is necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/supportsadvisorykeys)*