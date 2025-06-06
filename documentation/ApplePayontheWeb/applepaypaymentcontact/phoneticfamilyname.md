# phoneticFamilyName

**Framework**: Apple Pay on the Web  
**Kind**: property

The phonetic spelling of the contact’s family name.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString phoneticFamilyName;
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)

#### Discussion

Typically, you use phonetic names for transactions in Japan.

If your site requires the contact’s phonetic name, include this field in the [`requiredBillingContactFields`](applepaypaymentrequest/requiredbillingcontactfields.md) or [`requiredShippingContactFields`](applepaypaymentrequest/requiredshippingcontactfields.md) in your payment request.

Available in Apple Pay version 3. For more information about versions, see doc://com.apple.documentation/documentation/apple_pay_on_the_web/apple_pay_on_the_web_version_history.

## See Also

- [phoneNumber](applepaypaymentcontact/phonenumber.md)
  A phone number for the contact.
- [emailAddress](applepaypaymentcontact/emailaddress.md)
  An email address for the contact.
- [givenName](applepaypaymentcontact/givenname.md)
  The contact’s given name.
- [familyName](applepaypaymentcontact/familyname.md)
  The contact’s family name.
- [phoneticGivenName](applepaypaymentcontact/phoneticgivenname.md)
  The phonetic spelling of the contact’s given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentcontact/phoneticfamilyname)*