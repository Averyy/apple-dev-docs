# CTTelephonyNetworkInfo.RadioAccessTechnologyDidChangeMessage

**Framework**: Core Telephony  
**Kind**: struct

A message that posts when the radio access technology changes for one of the services.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct RadioAccessTechnologyDidChangeMessage
```

#### Overview

Use the [`serviceIdentifier`](cttelephonynetworkinfo/radioaccesstechnologydidchangemessage/serviceidentifier.md) property  as the key in [`serviceCurrentRadioAccessTechnology`](cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md) to get the value of the new radio access technology for the service.

## Topics

### Instance Properties
- [var serviceIdentifier: String](cttelephonynetworkinfo/radioaccesstechnologydidchangemessage/serviceidentifier.md)
  The service identifier for which the radio access technology changed.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../foundation/notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/radioaccesstechnologydidchangemessage)*