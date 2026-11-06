# supportsAdvisoryKeys

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the session supports advisory keys.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
var supportsAdvisoryKeys: Bool { get set }
```

```objc
@property (readwrite) BOOL supportsAdvisoryKeys;
```

## Discussion

Advisory keys are content keys that the key server sends before a client requests them. When you enable advisory keys, FairPlay can cache these keys and use them to fulfill later key requests without a round trip to the key server.

The default value is `false`. After you set this property to `true`, you can’t set it back to `false`. Attempting to do so throws an exception.

Important: When this property is `true`, use `makeOptionalStreamingContentKeyRequestDataForApp` to request key data. Calling `makeStreamingContentKeyRequestDataForApp` throws an exception.

If FairPlay already has a cached advisory key for a request, the completion handler receives `nil` key request data, and the request’s `canBeFulfilledWithAdvisoryKey` property is `true`. In this case, don’t send a request to the key server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/supportsadvisorykeys)*