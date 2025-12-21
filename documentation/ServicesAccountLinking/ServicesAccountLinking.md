# ServicesAccountLinking

**Framework**: ServicesAccountLinking  
**Kind**: module

Link reseller accounts with Apple Media & Purchases accounts.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

#### Overview

This framework enables applications to register reseller account identifiers or tokens with a user’s Apple Media & Purchases account. This functionality lets content providers and channel partners link their user accounts with Apple’s ecosystem.

To use this framework:

- Your application is enrolled in Apple’s channel partnership program.
- You have obtained partner credentials for generating tokens or identifiers.
- Your project targets iOS 16.4 or later.

If your application isn’t registered as an authorized partner, registration fails with a [`notEligible`](registrationerror/noteligible.md) error.  Contact the Apple channel partnership program to become an authorized partner.

## Topics

### Registration
- [struct ResellerAccount](reselleraccount.md)
  Reseller account type for linking with Apple Media & Purchases accounts.
### Error handling
- [struct RegistrationError](registrationerror.md)
  Registration error codes.
- [let RegistrationErrorDomain: String](registrationerrordomain.md)
  Error domain for account registration failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ServicesAccountLinking)*