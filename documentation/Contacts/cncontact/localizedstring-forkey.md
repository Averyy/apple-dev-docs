# localizedString(forKey:)

**Framework**: Contacts  
**Kind**: method

Returns a string containing the localized contact property name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func localizedString(forKey key: String) -> String
```

#### Return Value

A localized string containing the contact property name.

#### Discussion

This method returns a localized string for a contact property key. For example, the value of a Canadian `CNContactPostalAddressesKey` field would be “Postal Code”, while the value of a French one would be “Code Postal”.

## Parameters

- `key`: A string containing the contact property key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/localizedstring(forkey:))*