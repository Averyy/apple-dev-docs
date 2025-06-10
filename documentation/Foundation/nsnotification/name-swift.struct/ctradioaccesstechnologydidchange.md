# CTRadioAccessTechnologyDidChange

**Framework**: Foundation  
**Kind**: property

The name of the notification indicating that the radio access technology changed for one of the services.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static let CTRadioAccessTechnologyDidChange: NSNotification.Name
```

#### Discussion

The notification’s [`object`](nsnotification/object.md) is an [`NSString`](nsstring.md) that represents the service identifier of the service whose radio access technology has changed. Use this string as the key in [`serviceCurrentRadioAccessTechnology`](https://developer.apple.com/documentation/CoreTelephony/CTTelephonyNetworkInfo/serviceCurrentRadioAccessTechnology) to get the value of the new radio access technology for the service.

## See Also

- [static let CTServiceRadioAccessTechnologyDidChange: NSNotification.Name](nsnotification/name-swift.struct/ctserviceradioaccesstechnologydidchange.md)
  A notification that posts when radio access technology changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/ctradioaccesstechnologydidchange)*