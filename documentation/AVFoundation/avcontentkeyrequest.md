# AVContentKeyRequest

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that encapsulates information about a content decryption key request issued from a content key session object.

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
class AVContentKeyRequest
```

```objc
@interface AVContentKeyRequest : NSObject
```

## Topics

### Getting content key request data
- [func makeStreamingContentKeyRequestData(forApp: Data, contentIdentifier: Data?, options: [String : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](./avcontentkeyrequest/makestreamingcontentkeyrequestdata%28forapp,contentidentifier,options,completionhandler%29.md)
  Obtains encrypted key request data for a specific combination of app and content.
- [let AVContentKeyRequestProtocolVersionsKey: String](./avcontentkeyrequestprotocolversionskey.md)
  A key that specifies the versions of the content protection protocol supported by the application.
- [let AVContentKeyRequestRequiresValidationDataInSecureTokenKey: String](./avcontentkeyrequestrequiresvalidationdatainsecuretokenkey.md)
  A key that requires the secure token to have extended validation data.
- [let AVContentKeyRequestRandomDeviceIdentifierSeedKey: String](./avcontentkeyrequestrandomdeviceidentifierseedkey.md)
  Value is an NSData containing a 16-byte seed to randomize the user’s deviceID contained in the SPC blob during FairPlay key exchange
- [let AVContentKeyRequestShouldRandomizeDeviceIdentifierKey: String](./avcontentkeyrequestshouldrandomizedeviceidentifierkey.md)
  Value is an Boolean indicating whether the user’s deviceID contained in the SPC blob during FairPlay key exchange should be randomized using a system generated seed
### Responding to the content key request
- [func processContentKeyResponse(AVContentKeyResponse)](./avcontentkeyrequest/processcontentkeyresponse%28_%29.md)
  Sends the specified content key response to the receiver for processing.
- [func processContentKeyResponseError(any Error)](./avcontentkeyrequest/processcontentkeyresponseerror%28_%29.md)
  Tells the receiver that the app was unable to obtain a content key response.
- [func respondByRequestingPersistableContentKeyRequest()](./avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest%28%29.md)
  Tells the receiver that the app requires a persistable content key request object for processing.
### Getting content key request properties
- [var identifier: (any Sendable)?](./avcontentkeyrequest/identifier.md)
  The identifier for the content key.
- [var originatingRecipient: (any AVContentKeyRecipient)?](./avcontentkeyrequest/originatingrecipient.md)
  The AVContentKeyRecipient which initiated this request, if any.
- [var canProvidePersistableContentKey: Bool](./avcontentkeyrequest/canprovidepersistablecontentkey.md)
  The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [var error: (any Error)?](./avcontentkeyrequest/error.md)
  The error description for a failed key request.
- [var initializationData: Data?](./avcontentkeyrequest/initializationdata.md)
  The data used to obtain a key response.
- [var renewsExpiringResponseData: Bool](./avcontentkeyrequest/renewsexpiringresponsedata.md)
  A Boolean value that indicates whether the content key request renews previously provided response data.
- [var status: AVContentKeyRequest.Status](./avcontentkeyrequest/status-swift.property.md)
  The current state of the content key request.
- [AVContentKeyRequest.Status](./avcontentkeyrequest/status-swift.enum.md)
  The status for a content key request.
### Inspecting a request
- [var contentKey: AVContentKey?](./avcontentkeyrequest/contentkey.md)
  The generated content key.
- [var contentKeySpecifier: AVContentKeySpecifier](./avcontentkeyrequest/contentkeyspecifier.md)
  The requested content key specifier.
- [var options: [String : any Sendable]](./avcontentkeyrequest/options.md)
  A dictionary of options used to initialize key loading.
- [AVContentKeyRequest.RetryReason](./avcontentkeyrequest/retryreason.md)
  The reason for asking the client to retry a content key request.
### Instance Properties
- [var canBeFulfilledWithAdvisoryKey: Bool](./avcontentkeyrequest/canbefulfilledwithadvisorykey.md)
  Indicates whether this key request was initiated for an advisory key.
### Instance Methods
- [func makeOptionalStreamingContentKeyRequestData(forApp: Data, contentIdentifier: Data?, options: [String : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](./avcontentkeyrequest/makeoptionalstreamingcontentkeyrequestdata%28forapp,contentidentifier,options,completionhandler%29.md)
  Obtains an optional content key request data for a specific combination of application and content.
- [func respondByRequestingPersistableContentKeyRequestAndReturnError() throws](./avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequestandreturnerror%28%29.md)
  Tells the receiver that the app requires a persistable content key request object for processing.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVPersistableContentKeyRequest](./avpersistablecontentkeyrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### FairPlay streaming
- [class AVContentKeySession](./avcontentkeysession.md)
  An object that creates and tracks decryption keys for media data.
- [protocol AVContentKeySessionDelegate](./avcontentkeysessiondelegate.md)
  A protocol that handles content key requests.
- [class AVContentKey](./avcontentkey.md)
  An object that represents the content key decryptor.
- [class AVContentKeySpecifier](./avcontentkeyspecifier.md)
  An object that uniquely identifies a content key.
- [class AVPersistableContentKeyRequest](./avpersistablecontentkeyrequest.md)
  An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [class AVContentKeyResponse](./avcontentkeyresponse.md)
  An object that encapsulates information about a response to a content decryption key request.
- [enum AVExternalContentProtectionStatus](./avexternalcontentprotectionstatus.md)
  Constants that specify whether sufficient protection exists to display the content.
- [func AVSampleBufferAttachContentKey(CMSampleBuffer, AVContentKey, NSErrorPointer) -> Bool](./avsamplebufferattachcontentkey%28_,_,_%29.md)
  Attaches a content key to a sample buffer for the purpose of content decryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest)*