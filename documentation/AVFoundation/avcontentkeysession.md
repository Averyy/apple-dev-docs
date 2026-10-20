# AVContentKeySession

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that creates and tracks decryption keys for media data.

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
class AVContentKeySession
```

```objc
@interface AVContentKeySession : NSObject
```

## Topics

### Creating a session
- [convenience init(keySystem: AVContentKeySystem)](./avcontentkeysession/init%28keysystem%29.md)
  Creates a content key session to manage a collection of content decryption keys.
- [convenience init(keySystem: AVContentKeySystem, storageDirectoryAt: URL)](./avcontentkeysession/init%28keysystem,storagedirectoryat%29.md)
  Creates a content key session to manage a collection of content decryption keys; points to a directory that stores abnormal session termination reports.
### Inspecting the session
- [var keySystem: AVContentKeySystem](./avcontentkeysession/keysystem.md)
  The type of key system used to retrieve keys.
- [struct AVContentKeySystem](./avcontentkeysystem.md)
  A key-delivery method for a content key session.
- [var storageURL: URL?](./avcontentkeysession/storageurl.md)
  A URL that points to a writable storage directory.
### Managing the delegate object
- [func setDelegate((any AVContentKeySessionDelegate)?, queue: dispatch_queue_t?)](./avcontentkeysession/setdelegate%28_,queue%29.md)
  Sets the session’s delegate object and the dispatch queue on which to call the delegate’s methods.
- [var delegate: (any AVContentKeySessionDelegate)?](./avcontentkeysession/delegate.md)
  The content key session’s delegate object.
- [var delegateQueue: dispatch_queue_t?](./avcontentkeysession/delegatequeue.md)
  The dispatch queue the session uses to invoke delegate callbacks.
### Managing content key recipients
- [var contentKeyRecipients: [any AVContentKeyRecipient]](./avcontentkeysession/contentkeyrecipients.md)
  An array of content key recipients.
- [protocol AVContentKeyRecipient](./avcontentkeyrecipient.md)
  A protocol for requiring decryption keys for media data.
- [func addContentKeyRecipient(any AVContentKeyRecipient)](./avcontentkeysession/addcontentkeyrecipient%28_%29.md)
  Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.
- [func removeContentKeyRecipient(any AVContentKeyRecipient)](./avcontentkeysession/removecontentkeyrecipient%28_%29.md)
  Tells the delegate to remove the specified recipient.
### Processing requests
- [func processContentKeyRequest(withIdentifier: (any Sendable)?, initializationData: Data?, options: [String : any Sendable]?)](./avcontentkeysession/processcontentkeyrequest%28withidentifier,initializationdata,options%29.md)
  Tells the delegate to start loading the content decryption key with the specified identifier and initialization data.
### Managing expiration
- [func expire()](./avcontentkeysession/expire%28%29.md)
  Tells the delegate that the session expired as the result of normal, intentional processes.
- [func makeSecureTokenForExpirationDate(ofPersistableContentKey: Data, completionHandler: (Data?, (any Error)?) -> Void)](./avcontentkeysession/makesecuretokenforexpirationdate%28ofpersistablecontentkey,completionhandler%29.md)
  Creates a secure server playback context that the client sends to the key server to get an expiration date for the given persistable content key data.
- [func renewExpiringResponseData(for: AVContentKeyRequest)](./avcontentkeysession/renewexpiringresponsedata%28for%29.md)
  Tells the delegate that previously provided response data for a content key request is about to expire.
- [var contentProtectionSessionIdentifier: Data?](./avcontentkeysession/contentprotectionsessionidentifier.md)
  The identifier for the current content protection session.
### Invalidating content keys
- [func invalidatePersistableContentKey(Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](./avcontentkeysession/invalidatepersistablecontentkey%28_,options,completionhandler%29.md)
  Invalidates the persistable content key and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [func invalidateAllPersistableContentKeys(forApp: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](./avcontentkeysession/invalidateallpersistablecontentkeys%28forapp,options,completionhandler%29.md)
  Invalidates all of an app’s persistable content keys and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [struct AVContentKeySessionServerPlaybackContextOption](./avcontentkeysessionserverplaybackcontextoption.md)
  Options for specifying additional information for generating server playback context (SPC).
### Handling expired session reports
- [class func pendingExpiredSessionReports(withAppIdentifier: Data, storageDirectoryAt: URL) -> [Data]](./avcontentkeysession/pendingexpiredsessionreports%28withappidentifier,storagedirectoryat%29.md)
  Returns the expired session reports for content key sessions created with the specified app identifier.
- [class func removePendingExpiredSessionReports([Data], withAppIdentifier: Data, storageDirectoryAt: URL)](./avcontentkeysession/removependingexpiredsessionreports%28_,withappidentifier,storagedirectoryat%29.md)
  Removes expired session reports from storage.
### Initializers
- [convenience init(keySystem: AVContentKeySystem, storageDirectoryAtURL: URL)](./avcontentkeysession/init%28keysystem,storagedirectoryaturl%29.md)
### Instance Properties
- [var supportsAdvisoryKeys: Bool](./avcontentkeysession/supportsadvisorykeys.md)
  Boolean indicating whether advisory keys are enabled on the client.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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
- [protocol AVContentKeySessionDelegate](./avcontentkeysessiondelegate.md)
  A protocol that handles content key requests.
- [class AVContentKey](./avcontentkey.md)
  An object that represents the content key decryptor.
- [class AVContentKeySpecifier](./avcontentkeyspecifier.md)
  An object that uniquely identifies a content key.
- [class AVContentKeyRequest](./avcontentkeyrequest.md)
  An object that encapsulates information about a content decryption key request issued from a content key session object.
- [class AVPersistableContentKeyRequest](./avpersistablecontentkeyrequest.md)
  An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [class AVContentKeyResponse](./avcontentkeyresponse.md)
  An object that encapsulates information about a response to a content decryption key request.
- [enum AVExternalContentProtectionStatus](./avexternalcontentprotectionstatus.md)
  Constants that specify whether sufficient protection exists to display the content.
- [func AVSampleBufferAttachContentKey(CMSampleBuffer, AVContentKey, NSErrorPointer) -> Bool](./avsamplebufferattachcontentkey%28_,_,_%29.md)
  Attaches a content key to a sample buffer for the purpose of content decryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession)*