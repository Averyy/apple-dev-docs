# LACredentialType.applicationPassword

**Framework**: Local Authentication  
**Kind**: case

Specifies that a password is provided by the application.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case applicationPassword
```

#### Discussion

If not set, the user is prompted for their password when needed. When entered using the provided authentication dialog, the entered text is stored as UTF-8 encoded data.

## See Also

- [LACredentialType.smartCardPIN](lacredentialtype/smartcardpin.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacredentialtype/applicationpassword)*