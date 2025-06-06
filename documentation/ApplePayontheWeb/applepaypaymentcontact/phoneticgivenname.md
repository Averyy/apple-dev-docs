# phoneticGivenName

**Framework**: Apple Pay on the Web  
**Kind**: property

The phonetic spelling of the contact’s given name.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString phoneticGivenName;
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)

#### Discussion

Typically, you use phonetic names for transactions in Japan.

If your site requires the contact’s phonetic name, include this field in the [`requiredBillingContactFields`](applepaypaymentrequest/requiredbillingcontactfields.md) or [`requiredShippingContactFields`](applepaypaymentrequest/requiredshippingcontactfields.md) in your payment request.

Available in Apple Pay version 3.

## See Also

- [phoneNumber](applepaypaymentcontact/phonenumber.md)
  A phone number for the contact.
- [emailAddress](applepaypaymentcontact/emailaddress.md)
  An email address for the contact.
- [givenName](applepaypaymentcontact/givenname.md)
  The contact’s given name.
- [familyName](applepaypaymentcontact/familyname.md)
  The contact’s family name.
- [phoneticFamilyName](applepaypaymentcontact/phoneticfamilyname.md)
  The phonetic spelling of the contact’s family name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentcontact/phoneticgivenname)*