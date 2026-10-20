# CTServiceRadioAccessTechnologyDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notification that posts when radio access technology changes.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static let CTServiceRadioAccessTechnologyDidChange: NSNotification.Name
```

#### Discussion

The notification’s `object` is a string that represents the identifier of the service with changes to its radio access technology.  Use this identifier as the key in [`serviceCurrentRadioAccessTechnology`](../../../CoreTelephony/cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md) to get the value of the new radio access technology for the service.

## See Also

### Core Telephony
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](./ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/ctserviceradioaccesstechnologydidchange)*