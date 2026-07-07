# makeOptionalStreamingContentKeyRequestData(forApp:contentIdentifier:options:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Obtains an optional content key request data for a specific combination of application and content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
func makeOptionalStreamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier: Data?, options: [String : Any]? = nil) async throws -> Data
```

#### Discussion

This method generates key request data to be sent to a key server, with support for advisory key handling. When advisory keys are enabled (supportsAdvisoryKeys = YES), this method may return nil data without error if the requested key is already cached by the system, avoiding redundant server requests.

IMPORTANT: When supportsAdvisoryKeys is set to YES, this method MUST be used for all content key requests. The non-advisory variant is not compatible with advisory key handling and an exception will be thrown otherwise.

When the completion handler is called with nil data and nil error, check the canBeFulfilledWithAdvisoryKey property. A return value of YES indicates the key is already cached and no server communication is required.

## Parameters

- `appIdentifier`: An opaque identifier for the application. The contents and format are determined by the content protection system in use. An exception will be thrown if appIdentifier is nil.
- `contentIdentifier`: An optional opaque identifier for the content. The contents and format are determined by the content protection system in use.
- `options`: A dictionary of additional parameters required to obtain the key, or nil if none are needed. See AVContentKeyRequest Key constants.
- `completionHandler`: A block invoked when the request completes. Called with key request data for server communication or nil data if already fulfilled by an advisory key response; error, if creating the key request data failed. An exception will be thrown if completionHandler is nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/makeoptionalstreamingcontentkeyrequestdata(forapp:contentidentifier:options:completionhandler:))*