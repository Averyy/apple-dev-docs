# AVContentKeyRequestRequiresValidationDataInSecureTokenKey

**Framework**: AVFoundation  
**Kind**: var

A key that requires the secure token to have extended validation data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let AVContentKeyRequestRequiresValidationDataInSecureTokenKey: String
```

#### Discussion

You create the value for this key by using [`persistableContentKey(fromKeyVendorResponse:options:)`](avpersistablecontentkeyrequest/persistablecontentkey(fromkeyvendorresponse:options:).md).

## See Also

- [func makeStreamingContentKeyRequestData(forApp: Data, contentIdentifier: Data?, options: [String : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp:contentidentifier:options:completionhandler:).md)
  Obtains encrypted key request data for a specific combination of app and content.
- [let AVContentKeyRequestProtocolVersionsKey: String](avcontentkeyrequestprotocolversionskey.md)
  A key that specifies the versions of the content protection protocol supported by the application.
- [let AVContentKeyRequestRandomDeviceIdentifierSeedKey: String](avcontentkeyrequestrandomdeviceidentifierseedkey.md)
  Value is an NSData containing a 16-byte seed to randomize the user’s deviceID contained in the SPC blob during FairPlay key exchange
- [let AVContentKeyRequestShouldRandomizeDeviceIdentifierKey: String](avcontentkeyrequestshouldrandomizedeviceidentifierkey.md)
  Value is an Boolean indicating whether the user’s deviceID contained in the SPC blob during FairPlay key exchange should be randomized using a system generated seed


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequestrequiresvalidationdatainsecuretokenkey)*