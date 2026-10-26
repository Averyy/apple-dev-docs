# INIntentError

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Errors returned by SiriKit.

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
struct INIntentError
```

## Topics

### Encoding Errors
- [static var decodingGeneric: INIntentError.Code](./inintenterror/decodinggeneric.md)
- [static var encodingFailed: INIntentError.Code](./inintenterror/encodingfailed.md)
- [static var encodingGeneric: INIntentError.Code](./inintenterror/encodinggeneric.md)
### Image Errors
- [static var imageGeneric: INIntentError.Code](./inintenterror/imagegeneric.md)
- [static var imageLoadingFailed: INIntentError.Code](./inintenterror/imageloadingfailed.md)
- [static var imageNoServiceAvailable: INIntentError.Code](./inintenterror/imagenoserviceavailable.md)
- [static var imageServiceFailure: INIntentError.Code](./inintenterror/imageservicefailure.md)
- [static var imageProxyInvalid: INIntentError.Code](./inintenterror/imageproxyinvalid.md)
- [static var imageProxyLoop: INIntentError.Code](./inintenterror/imageproxyloop.md)
- [static var imageProxyTimeout: INIntentError.Code](./inintenterror/imageproxytimeout.md)
- [static var imageRetrievalFailed: INIntentError.Code](./inintenterror/imageretrievalfailed.md)
- [static var imageStorageFailed: INIntentError.Code](./inintenterror/imagestoragefailed.md)
- [static var imageScalingFailed: INIntentError.Code](./inintenterror/imagescalingfailed.md)
- [static var permissionDenied: INIntentError.Code](./inintenterror/permissiondenied.md)
### App Intent Errors
- [static var noAppIntent: INIntentError.Code](./inintenterror/noappintent.md)
- [static var unableToCreateAppIntentRepresentation: INIntentError.Code](./inintenterror/unabletocreateappintentrepresentation.md)
### Voice Shortcut Errors
- [static var voiceShortcutCreationFailed: INIntentError.Code](./inintenterror/voiceshortcutcreationfailed.md)
- [static var voiceShortcutDeleteFailed: INIntentError.Code](./inintenterror/voiceshortcutdeletefailed.md)
- [static var voiceShortcutGetFailed: INIntentError.Code](./inintenterror/voiceshortcutgetfailed.md)
### Interaction Errors
- [static var interactionOperationNotSupported: INIntentError.Code](./inintenterror/interactionoperationnotsupported.md)
  The [`INInteraction`](./ininteraction.md) object could not be donated or deleted because those capabilities are not supported on the current device.
- [static var donatingInteraction: INIntentError.Code](./inintenterror/donatinginteraction.md)
  The [`INInteraction`](./ininteraction.md) object could not be donated to the system.
- [static var deletingAllInteractions: INIntentError.Code](./inintenterror/deletingallinteractions.md)
  The system was unable to delete all donated [`INInteraction`](./ininteraction.md) objects.
- [static var deletingInteractionWithIdentifiers: INIntentError.Code](./inintenterror/deletinginteractionwithidentifiers.md)
  The system was unable to delete the specified set of [`INInteraction`](./ininteraction.md) objects.
- [static var deletingInteractionWithGroupIdentifier: INIntentError.Code](./inintenterror/deletinginteractionwithgroupidentifier.md)
  The system was unable to delete the [`INInteraction`](./ininteraction.md) objects using their group identifier.
### Extension Errors
- [static var intentSupportedByMultipleExtension: INIntentError.Code](./inintenterror/intentsupportedbymultipleextension.md)
  An intent was supported by more than one Intents extension in the same app.
- [static var restrictedIntentsNotSupportedByExtension: INIntentError.Code](./inintenterror/restrictedintentsnotsupportedbyextension.md)
  An intent was listed in the `IntentsRestrictedWhileLocked` key of the app’s `Info.plist`, but not in the `IntentsSupported` key.
- [static var noHandlerProvidedForIntent: INIntentError.Code](./inintenterror/nohandlerprovidedforintent.md)
  No object was provided to handle the specified intent.
- [static var invalidIntentName: INIntentError.Code](./inintenterror/invalidintentname.md)
  The extension declared support for a nonexistent intent.
- [static var noAppAvailable: INIntentError.Code](./inintenterror/noappavailable.md)
- [static var extensionLaunchingTimeout: INIntentError.Code](./inintenterror/extensionlaunchingtimeout.md)
  The extension failed to launch in a timely manner.
- [static var extensionBringUpFailed: INIntentError.Code](./inintenterror/extensionbringupfailed.md)
  There was an error while trying to communicate with the extension.
### Other Errors
- [static var invalidUserVocabularyFileLocation: INIntentError.Code](./inintenterror/invaliduservocabularyfilelocation.md)
  An invalid location was specified for the user vocabulary file.
- [static var requestTimedOut: INIntentError.Code](./inintenterror/requesttimedout.md)
  The underlying request timed out.
- [static var missingInformation: INIntentError.Code](./inintenterror/missinginformation.md)
### General Error
- [static var errorDomain: String](./inintenterror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [INIntentError.Code](./inintenterror/code.md)
  Constants for error codes returned by the framework.
- [let INIntentErrorDomain: String](./inintenterrordomain.md)
  The error domain for the Intents framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenterror)*