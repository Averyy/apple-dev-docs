# addressDictionary

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A dictionary containing the Address Book keys and values for the placemark.

**Availability**:
- iOS 5.0+ - Deprecated in 11.0
- iPadOS 5.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- watchOS 1.0+ - Deprecated in 4.0

> **Deprecated**: Use [`CLPlacemark`](../clplacemark.md) instead of Address Book.

## Declaration

```swift
var addressDictionary: [AnyHashable : Any]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDictionary * addressDictionary;
```

## Discussion

The keys in this dictionary are those defined by the Address Book framework and used to access address information for a person. For a list of the strings that can be in this dictionary, see the “Address Property” constants in `ABPerson`.

You can format the contents of this dictionary to get a full address string as opposed to building the address yourself. To format the dictionary, use the [`ABCreateStringWithAddressDictionary(_:_:)`](../../AddressBookUI/abcreatestringwithaddressdictionary%28_,_%29.md) function as described in `AddressBookUI Functions`.

## See Also

### Getting the associated contact details
- [var postalAddress: CNPostalAddress?](./postaladdress.md)
  The postal address associated with the location, formatted for use with the Contacts framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/addressdictionary)*