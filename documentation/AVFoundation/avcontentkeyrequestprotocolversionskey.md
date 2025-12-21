# AVContentKeyRequestProtocolVersionsKey

**Framework**: AVFoundation  
**Kind**: var

A key that specifies the versions of the content protection protocol supported by the application.

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
let AVContentKeyRequestProtocolVersionsKey: String
```

#### Discussion

The contents of this key are an [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) or one or more [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects.

## See Also

- [func makeStreamingContentKeyRequestData(forApp: Data, contentIdentifier: Data?, options: [String : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp:contentidentifier:options:completionhandler:).md)
  Obtains encrypted key request data for a specific combination of app and content.
- [let AVContentKeyRequestRequiresValidationDataInSecureTokenKey: String](avcontentkeyrequestrequiresvalidationdatainsecuretokenkey.md)
  A key that requires the secure token to have extended validation data.
- [let AVContentKeyRequestRandomDeviceIdentifierSeedKey: String](avcontentkeyrequestrandomdeviceidentifierseedkey.md)
  Value is an NSData containing a 16-byte seed to randomize the user’s deviceID contained in the SPC blob during FairPlay key exchange
- [let AVContentKeyRequestShouldRandomizeDeviceIdentifierKey: String](avcontentkeyrequestshouldrandomizedeviceidentifierkey.md)
  Value is an Boolean indicating whether the user’s deviceID contained in the SPC blob during FairPlay key exchange should be randomized using a system generated seed


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequestprotocolversionskey)*