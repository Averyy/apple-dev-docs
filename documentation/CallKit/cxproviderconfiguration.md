# CXProviderConfiguration

**Framework**: CallKit  
**Kind**: class

An encapsulation of the configuration of a provider object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXProviderConfiguration
```

#### Overview

A [`CXProviderConfiguration`](cxproviderconfiguration.md) object controls the native call UI for incoming and outgoing calls, including a localized name for the provider, the ringtone to play for incoming calls, and the icon to display during calls. A provider configuration can also set the maximum number of call groups and the number of calls in a single call group, determine whether to use emails and phone numbers as handles, and specify whether to support video.

## Topics

### Creating New Configurations
- [init()](cxproviderconfiguration/init.md)
  Creates the configuration of a provider object.
- [convenience init(localizedName: String)](cxproviderconfiguration/init(localizedname:).md)
  Initializes a configuration with the specified localized name.
### Configuring Native Call UI
- [var localizedName: String?](cxproviderconfiguration/localizedname.md)
  The localized name of the provider.
- [var ringtoneSound: String?](cxproviderconfiguration/ringtonesound.md)
  The name of the sound resource in the app bundle to be used for the provider ringtone.
- [var iconTemplateImageData: Data?](cxproviderconfiguration/icontemplateimagedata.md)
  The PNG data for the icon image to be displayed for the provider.
### Configuring Call Capabilities
- [var maximumCallGroups: Int](cxproviderconfiguration/maximumcallgroups.md)
  The maximum number of call groups.
- [var maximumCallsPerCallGroup: Int](cxproviderconfiguration/maximumcallspercallgroup.md)
  The maximum number of calls per call group.
- [var supportedHandleTypes: Set<CXHandle.HandleType>](cxproviderconfiguration/supportedhandletypes-kd6i.md)
  The supported handle types.
- [var supportsVideo: Bool](cxproviderconfiguration/supportsvideo.md)
  A Boolean value that indicates whether the provider supports video in addition to audio.
- [var includesCallsInRecents: Bool](cxproviderconfiguration/includescallsinrecents.md)
  A Boolean value that indicates whether the provider includes a call in the system’s Recents list after the call ends.
### Instance Properties
- [var supportsAudioTranslation: Bool](cxproviderconfiguration/supportsaudiotranslation.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CXProvider](cxprovider.md)
  An object that represents a telephony provider.
- [protocol CXProviderDelegate](cxproviderdelegate.md)
  A collection of methods that a telephony provider object calls.
- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)
  Initiate outgoing calls with VoIP and configure your app to receive incoming calls.
- [VoIP calling with CallKit](voip-calling-with-callkit.md)
  Use the CallKit framework to integrate native VoIP calling.
- [Preparing your app to be the default calling app](preparing-your-app-to-be-the-default-calling-app.md)
  Configure your CallKit or LiveCommunicationKit app so people can set it as the default calling app on their device.
- [CallKit updates](../Updates/CallKit.md)
  Learn about important changes to CallKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderconfiguration)*