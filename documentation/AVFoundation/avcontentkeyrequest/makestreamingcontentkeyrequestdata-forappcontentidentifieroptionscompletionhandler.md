# makeStreamingContentKeyRequestData(forApp:contentIdentifier:options:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Obtains encrypted key request data for a specific combination of app and content.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func makeStreamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier: Data?, options: [String : Any]? = nil) async throws -> Data
```

#### Discussion

If [`AVContentKeyRequestProtocolVersionsKey`](avcontentkeyrequestprotocolversionskey.md) is not specified in the `options` parameter, the default protocol of `1` is used.

## Parameters

- `appIdentifier`: An opaque identifier for the app.
- `contentIdentifier`: An opaque identifier for the content.
- `options`: A dictionary containing any additional information required to obtain the key. The value of this parameter is   when no additional information is required.
- `handler`: A block called after the streaming content key request has been prepared.

## See Also

- [let AVContentKeyRequestProtocolVersionsKey: String](avcontentkeyrequestprotocolversionskey.md)
  A key that specifies the versions of the content protection protocol supported by the application.
- [let AVContentKeyRequestRequiresValidationDataInSecureTokenKey: String](avcontentkeyrequestrequiresvalidationdatainsecuretokenkey.md)
  A key that requires the secure token to have extended validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp:contentidentifier:options:completionhandler:))*