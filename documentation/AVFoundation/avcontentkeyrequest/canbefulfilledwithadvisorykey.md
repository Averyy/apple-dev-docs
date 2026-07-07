# canBeFulfilledWithAdvisoryKey

**Framework**: AVFoundation  
**Kind**: property

Indicates whether this key request was initiated for an advisory key.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var canBeFulfilledWithAdvisoryKey: Bool { get }
```

#### Discussion

This property is set to true when: 1. Advisory key loading is enabled on the parent AVContentKeySession 2. The key was previously loaded as an advisory key and cached by FairPlay 3. A subsequent request for the same key is made

When `canBeFulfilledWithAdvisoryKey` is true and `makeStreamingContentKeyRequestData` returns nil for the key request data, this indicates FairPlay has already cached the key. No request to the key server for a key response is necessary, and the application should simply return from the completion handler.

This property should be checked in the completion handler of `makeStreamingContentKeyRequestData(forApp:contentIdentifier:options:completionHandler:)` whenever the key request data is nil to distinguish advisory keys from actual errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/canbefulfilledwithadvisorykey)*