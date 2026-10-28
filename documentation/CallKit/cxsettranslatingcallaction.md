# CXSetTranslatingCallAction

**Framework**: CallKit  
**Kind**: class  
**Role**: Class

An encapsulation of the act of translating a call.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class CXSetTranslatingCallAction
```

```objc
@interface CXSetTranslatingCallAction : CXCallAction
```

## Overview

[`CXSetTranslatingCallAction`](./cxsettranslatingcallaction.md) is a concrete subclass of [`CXCallAction`](./cxcallaction.md). When a caller chooses to translate a conversation, the system provides translated captions, and a translated transcript of the call and the [`CXProvider`](./cxprovider.md) sends the [`provider(_:perform:)`](./cxproviderdelegate/provider%28_,perform%29-43atg.md) to its delegate. The provider’s delegate calls the [`fulfill()`](./cxaction/fulfill%28%29.md) method to indicate that the action was successfully performed.

> ❗ **Important**: To avoid interrupting or impeding call translation when a person mutes their audio during a conversation, don’t deactivate the upstream audio. Instead, mute your app’s audio input using [`CXSetMutedCallAction`](./cxsetmutedcallaction.md) and keep the upstream audio active to allow translated audio to flow when a person mutes the hardware microphone.

## Topics

### Creating New Actions
- [init?(coder: NSCoder)](./cxsettranslatingcallaction/init%28coder%29.md)
  Creates a new action to start or stop translating a call with the provided data.
### Accessing Action Attributes
- [var isTranslating: Bool](./cxsettranslatingcallaction/istranslating.md)
  A value that indicates whether translation is active for a call.
### Completing Actions
- [enum CXTranslationEngine](./cxtranslationengine.md)
  Values that describe the translation engine that provided a translation.
### Initializers
- [init(call: UUID, isTranslating: Bool, localLanguage: String, remoteLanguage: String)](./cxsettranslatingcallaction/init%28call,istranslating,locallanguage,remotelanguage%29.md)
- [init(callUUID: UUID, isTranslating: Bool, localLanguage: String, remoteLanguage: String)](./cxsettranslatingcallaction/init%28calluuid,istranslating,locallanguage,remotelanguage%29.md)
### Instance Properties
- [var localLanguage: String](./cxsettranslatingcallaction/locallanguage.md)
- [var remoteLanguage: String](./cxsettranslatingcallaction/remotelanguage.md)
### Instance Methods
- [func fulfill(using: CXTranslationEngine)](./cxsettranslatingcallaction/fulfill%28using%29.md)

## Relationships

### Inherits From
- [CXCallAction](./cxcallaction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Call-related actions
- [class CXAction](./cxaction.md)
  An abstract class that declares a programmatic interface for objects that represent a telephony action.
- [class CXCallAction](./cxcallaction.md)
  A programmatic interface for objects that represent a telephony action associated with a call object.
- [class CXEndCallAction](./cxendcallaction.md)
  An encapsulation of the act of ending a call.
- [class CXPlayDTMFCallAction](./cxplaydtmfcallaction.md)
  An encapsulation of the act of playing a dual tone multifrequency (DTMF) sequence.
- [class CXSetGroupCallAction](./cxsetgroupcallaction.md)
  An encapsulation of the act of grouping or ungrouping calls.
- [class CXSetHeldCallAction](./cxsetheldcallaction.md)
  An encapsulation of the act of placing a call on hold or removing a call from hold.
- [class CXSetMutedCallAction](./cxsetmutedcallaction.md)
  An encapsulation of the act of muting or unmuting a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsettranslatingcallaction)*