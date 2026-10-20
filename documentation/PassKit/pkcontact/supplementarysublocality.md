# supplementarySubLocality

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The contact’s sublocality, or `nil` if the sublocality is not needed for the transaction.

**Availability**:
- iOS 9.2+ - Deprecated in 10.3
- iPadOS 9.2+ - Deprecated in 10.3
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.2

> **Deprecated**: Use subLocality and subAdministrativeArea on -postalAddress instead

## Declaration

```swift
var supplementarySubLocality: String? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSString * supplementarySubLocality;
```

#### Discussion

If the transaction requires the contact’s address, and the region requires a sublocality, then the Apple Pay sheet automatically prompts the user to enter their sublocality. The contact’s sublocality information is stored in this property.

## See Also

### Contact information
- [var emailAddress: String?](./emailaddress.md)
  The contact’s email address, or `nil` if the contact’s email is not needed for the transaction.
- [var name: PersonNameComponents?](./name.md)
  The contact’s first and last name, or `nil` if the contact’s name is not needed for the transaction.
- [var phoneNumber: CNPhoneNumber?](./phonenumber.md)
  The contact’s telephone number, or `nil` if the contact’s phone number is not needed for the transaction.
- [var postalAddress: CNPostalAddress?](./postaladdress.md)
  The contact’s full postal address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkcontact/supplementarysublocality)*