# CNInstantMessageAddress

**Framework**: Contacts  
**Kind**: class

An immutable object representing an instant message address for the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNInstantMessageAddress
```

#### Overview

Use the methods and properties of `CNInstantMessageAddress` to identify instant messaging addresses. Some instant message services, such as Facebook and Skype are predefined in this class. You can also specify your own instant message service using the [`init(username:service:)`](cninstantmessageaddress/init(username:service:).md) method.

`CNInstantMessageAddress` objects are thread-safe, and you may access their properties from any thread of your app.

## Topics

### Creating an Instant Message Address
- [init(username: String, service: String)](cninstantmessageaddress/init(username:service:).md)
  Returns a [`CNInstantMessageAddress`](cninstantmessageaddress.md) object initialized with the specified user name and service.
### Getting the Address Information
- [var service: String](cninstantmessageaddress/service.md)
  The name of the instant message address service.
- [var username: String](cninstantmessageaddress/username.md)
  The user name for instant message service address.
### Getting Localized Address Information
- [class func localizedString(forKey: String) -> String](cninstantmessageaddress/localizedstring(forkey:).md)
  Returns a string containing the localized property name.
- [let CNInstantMessageAddressUsernameKey: String](cninstantmessageaddressusernamekey.md)
  Instant message address username key.
- [let CNInstantMessageAddressServiceKey: String](cninstantmessageaddressservicekey.md)
  Instant message address service key.
### Getting Localized Service Names
- [class func localizedString(forService: String) -> String](cninstantmessageaddress/localizedstring(forservice:).md)
  Returns a string containing the localized name of the specified service.
- [let CNInstantMessageServiceAIM: String](cninstantmessageserviceaim.md)
  Instant message service for AIM.
- [let CNInstantMessageServiceFacebook: String](cninstantmessageservicefacebook.md)
  Instant message service for Facebook.
- [let CNInstantMessageServiceGaduGadu: String](cninstantmessageservicegadugadu.md)
  Instant message service for Gadu Gadu.
- [let CNInstantMessageServiceGoogleTalk: String](cninstantmessageservicegoogletalk.md)
  Instant message service for Google Talk.
- [let CNInstantMessageServiceICQ: String](cninstantmessageserviceicq.md)
  Instant message service for ICQ.
- [let CNInstantMessageServiceJabber: String](cninstantmessageservicejabber.md)
  Instant message service for Jabber.
- [let CNInstantMessageServiceMSN: String](cninstantmessageservicemsn.md)
  Instant message service for MSN.
- [let CNInstantMessageServiceQQ: String](cninstantmessageserviceqq.md)
  Instant message service for QQ.
- [let CNInstantMessageServiceSkype: String](cninstantmessageserviceskype.md)
  Instant message service for Skype.
- [let CNInstantMessageServiceYahoo: String](cninstantmessageserviceyahoo.md)
  Instant message service for Yahoo.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CNPostalAddress](cnpostaladdress.md)
  An immutable representation of the postal address for a contact.
- [class CNMutablePostalAddress](cnmutablepostaladdress.md)
  A mutable representation of the postal address for a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cninstantmessageaddress)*