# canBeFulfilledWithAdvisoryKey

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a cached advisory key can fulfill the key request.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
var canBeFulfilledWithAdvisoryKey: Bool { get }
```

```objc
@property (readonly) BOOL canBeFulfilledWithAdvisoryKey;
```

## Discussion

The value of this property is `true` when all of the following conditions are met:

- The AVContentKeySession `supportsAdvisoryKeys` property is `true`.
- FairPlay previously loaded and cached the key as an advisory key.
- The app makes a subsequent request for the same key.

Check this property in the completion handler of `makeOptionalStreamingContentKeyRequestDataForApp` when the key request data is `nil`. A value of `true` means FairPlay already has the key cached, and no further action is necessary. A value of `false` means the request failed, so inspect the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/canbefulfilledwithadvisorykey)*