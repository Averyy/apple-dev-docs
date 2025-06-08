# CallKit

**Framework**: CallKit  
**Kind**: module

Display the system-calling UI for your app’s VoIP services, and coordinate your calling services with other apps and the system.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Mentions

- [Sending End-to-End Encrypted VoIP Calls](sending-end-to-end-encrypted-voip-calls.md)
- [Preparing your app to be the default calling app](preparing-your-app-to-be-the-default-calling-app.md)

#### Overview

Use CallKit to integrate your calling services with other call-related apps in the system. CallKit provides the calling interface, and you handle the back-end communication with your VoIP service. See [`Making and receiving VoIP calls`](making-and-receiving-voip-calls.md) for more information.

For incoming and outgoing calls, CallKit displays the same interfaces as the Phone app, giving your app a more native look and feel. CallKit also responds appropriately to system-level behaviors, such as Do Not Disturb.

In addition to handling calls, you can use a Call Directory app extension to provide caller ID information and a list of blocked numbers associated with your service. See [`Identifying and blocking calls`](identifying-and-blocking-calls.md) for more information.

##### Manage User Privacy

With a person’s permission, an installed health research app that uses [`SensorKit`](https://developer.apple.com/documentation/SensorKit) entitlements may collect Speech Metrics data while your CallKit app is in use. To prevent this, you can set the [`SRResearchDataGeneration`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SRResearchDataGeneration) information property list key to `NO`.

> ❗ **Important**:  When a person makes a call in your app that uses CallKit, your app provides the contact information of the recipient to the system. The system may use that information to indicate communication with that person as a suggestion in the Journal app, or in other apps that use the [`Journaling Suggestions`](https://developer.apple.com/documentation/JournalingSuggestions) framework.

##### Become the Default Calling App

In iOS and iPadOS 18.2 and later, a person may select an app — other than the Phone app or FaceTime — to place calls by default. To make your CallKit or [`LiveCommunicationKit`](https://developer.apple.com/documentation/LiveCommunicationKit) app support the default calling app setting, see [`Preparing your app to be the default calling app`](preparing-your-app-to-be-the-default-calling-app.md).

## Topics

### Essentials
- [class CXProvider](cxprovider.md)
  An object that represents a telephony provider.
- [protocol CXProviderDelegate](cxproviderdelegate.md)
  A collection of methods that a telephony provider object calls.
- [class CXProviderConfiguration](cxproviderconfiguration.md)
  An encapsulation of the configuration of a provider object.
- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)
  Initiate outgoing calls with VoIP and configure your app to receive incoming calls.
- [VoIP calling with CallKit](voip-calling-with-callkit.md)
  Use the CallKit framework to integrate native VoIP calling.
- [Preparing your app to be the default calling app](preparing-your-app-to-be-the-default-calling-app.md)
  Configure your CallKit or LiveCommunicationKit app so people can set it as the default calling app on their device.
### Incoming calls
- [Responding to VoIP Notifications from PushKit](../PushKit/responding-to-voip-notifications-from-pushkit.md)
  Receive incoming Voice-over-IP (VoIP) push notifications and use them to display the system call interface to the user.
- [class CXCallUpdate](cxcallupdate.md)
  An encapsulation of new and changed information about a call.
- [class CXAnswerCallAction](cxanswercallaction.md)
  An encapsulation of the act of answering an incoming call.
### Outgoing calls
- [Sending End-to-End Encrypted VoIP Calls](sending-end-to-end-encrypted-voip-calls.md)
  Initiate VoIP calls when your server can’t determine whether an outgoing notification is a request for a VoIP call due to metadata encryption.
- [class CXCallController](cxcallcontroller.md)
  A programmatic interface for interacting with and observing calls.
- [class CXTransaction](cxtransaction.md)
  An object that contains zero or more action objects for a call controller to perform.
- [class CXStartCallAction](cxstartcallaction.md)
  An encapsulation of the act of initiating an outgoing call.
### Call-related actions
- [class CXAction](cxaction.md)
  An abstract class that declares a programmatic interface for objects that represent a telephony action.
- [class CXCallAction](cxcallaction.md)
  A programmatic interface for objects that represent a telephony action associated with a call object.
- [class CXEndCallAction](cxendcallaction.md)
  An encapsulation of the act of ending a call.
- [class CXPlayDTMFCallAction](cxplaydtmfcallaction.md)
  An encapsulation of the act of playing a dual tone multifrequency (DTMF) sequence.
- [class CXSetGroupCallAction](cxsetgroupcallaction.md)
  An encapsulation of the act of grouping or ungrouping calls.
- [class CXSetHeldCallAction](cxsetheldcallaction.md)
  An encapsulation of the act of placing a call on hold or removing a call from hold.
- [class CXSetMutedCallAction](cxsetmutedcallaction.md)
  An encapsulation of the act of muting or unmuting a call.
### Call information
- [class CXCall](cxcall.md)
  A telephony call.
- [class CXCallObserver](cxcallobserver.md)
  A programmatic interface for an object that manages a list of active calls and observes call changes.
- [protocol CXCallObserverDelegate](cxcallobserverdelegate.md)
  A collection of methods the system calls when a call changes state.
- [class CXHandle](cxhandle.md)
  A way to reach a call recipient, such as a phone number or email address.
### Caller ID
- [Identifying and blocking calls](identifying-and-blocking-calls.md)
  Create a Call Directory app extension to identify and block incoming callers by their phone number.
- [class CXCallDirectoryProvider](cxcalldirectoryprovider.md)
  The principal object for a Call Directory app extension for a host app.
- [class CXCallDirectoryExtensionContext](cxcalldirectoryextensioncontext.md)
  A programmatic interface for adding identification and blocking entries to a Call Directory app extension.
- [protocol CXCallDirectoryExtensionContextDelegate](cxcalldirectoryextensioncontextdelegate.md)
  A collection of methods a Call Directory extension context object calls when a request fails.
- [class CXCallDirectoryManager](cxcalldirectorymanager.md)
  The programmatic interface to an object that manages a Call Directory app extension.
### Reference
- [CallKit Enumerations](callkit-enumerations.md)
- [CallKit Constants](callkit-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CallKit)*