# INIntentError.Code

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants for error codes returned by the framework.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum Code
```

```c
enum INIntentErrorCode : NSInteger;
```

## Topics

### Encoding Errors
- [INIntentError.Code.decodingGeneric](./code/decodinggeneric.md)
- [INIntentError.Code.encodingFailed](./code/encodingfailed.md)
- [INIntentError.Code.encodingGeneric](./code/encodinggeneric.md)
### Image Errors
- [INIntentError.Code.imageGeneric](./code/imagegeneric.md)
- [INIntentError.Code.imageLoadingFailed](./code/imageloadingfailed.md)
- [INIntentError.Code.imageNoServiceAvailable](./code/imagenoserviceavailable.md)
- [INIntentError.Code.imageServiceFailure](./code/imageservicefailure.md)
- [INIntentError.Code.imageProxyInvalid](./code/imageproxyinvalid.md)
- [INIntentError.Code.imageProxyLoop](./code/imageproxyloop.md)
- [INIntentError.Code.imageProxyTimeout](./code/imageproxytimeout.md)
- [INIntentError.Code.imageRetrievalFailed](./code/imageretrievalfailed.md)
- [INIntentError.Code.imageStorageFailed](./code/imagestoragefailed.md)
- [INIntentError.Code.imageScalingFailed](./code/imagescalingfailed.md)
- [INIntentError.Code.permissionDenied](./code/permissiondenied.md)
### Voice Shortcut Errors
- [INIntentError.Code.voiceShortcutCreationFailed](./code/voiceshortcutcreationfailed.md)
- [INIntentError.Code.voiceShortcutDeleteFailed](./code/voiceshortcutdeletefailed.md)
- [INIntentError.Code.voiceShortcutGetFailed](./code/voiceshortcutgetfailed.md)
### Interaction Errors
- [INIntentError.Code.interactionOperationNotSupported](./code/interactionoperationnotsupported.md)
  The [`INInteraction`](../ininteraction.md) object could not be donated or deleted because those capabilities are not supported on the current device.
- [INIntentError.Code.donatingInteraction](./code/donatinginteraction.md)
  The INInteraction object could not be donated to the system.
- [INIntentError.Code.deletingAllInteractions](./code/deletingallinteractions.md)
  The system was unable to delete all donated INInteraction objects.
- [INIntentError.Code.deletingInteractionWithIdentifiers](./code/deletinginteractionwithidentifiers.md)
  The system was unable to delete the specified set of INInteraction objects.
- [INIntentError.Code.deletingInteractionWithGroupIdentifier](./code/deletinginteractionwithgroupidentifier.md)
  The system was unable to delete the INInteraction objects using their group identifier.
### Extension Errors
- [INIntentError.Code.extensionLaunchingTimeout](./code/extensionlaunchingtimeout.md)
  The extension failed to launch in a timely manner.
- [INIntentError.Code.extensionBringUpFailed](./code/extensionbringupfailed.md)
  There was an error while trying to communicate with the extension.
- [INIntentError.Code.noAppAvailable](./code/noappavailable.md)
- [INIntentError.Code.intentSupportedByMultipleExtension](./code/intentsupportedbymultipleextension.md)
  An intent was supported by more than one Intents extension in the same app. An app may have multiple Intents extensions, but each one must support a unique set of intents.
- [INIntentError.Code.restrictedIntentsNotSupportedByExtension](./code/restrictedintentsnotsupportedbyextension.md)
  An intent was listed in the `IntentsRestrictedWhileLocked` key of the app’s `Info.plist`, but not in the `IntentsSupported` key. All intents in the `IntentsRestrictedWhileLocked` key must also be present in the `IntentsSupported` key.
- [INIntentError.Code.noHandlerProvidedForIntent](./code/nohandlerprovidedforintent.md)
  No object was provided to handle the specified intent. If your extension declares support for an intent in its `Info.plist` file, the [`handler(for:)`](../inintenthandlerproviding/handler%28for%29.md) method of its [`INExtension`](../inextension.md) object must provide a corresponding handler object.
- [INIntentError.Code.invalidIntentName](./code/invalidintentname.md)
  The extension declared support for a nonexistent intent. Check your extension’s `Info.plist` file to make sure all intent names are spelled correctly.
### Other Errors
- [INIntentError.Code.requestTimedOut](./code/requesttimedout.md)
  The underlying request timed out.
- [INIntentError.Code.invalidUserVocabularyFileLocation](./code/invaliduservocabularyfilelocation.md)
  An invalid location was specified for the user vocabulary file.
- [INIntentError.Code.missingInformation](./code/missinginformation.md)
### Enumeration Cases
- [INIntentError.Code.noAppIntent](./code/noappintent.md)
- [INIntentError.Code.unableToCreateAppIntentRepresentation](./code/unabletocreateappintentrepresentation.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct INIntentError](../inintenterror.md)
  Errors returned by SiriKit.
- [let INIntentErrorDomain: String](../inintenterrordomain.md)
  The error domain for the Intents framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenterror/code)*