# formattedAddress(from:)

**Framework**: Address Book  
**Kind**: method

Returns an attributed string containing the formatted address.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func formattedAddress(from address: [AnyHashable : Any]!) -> NSAttributedString!
```

#### Return Value

An attributed string containing the formatted address.

#### Discussion

The string’s attributes match address dictionary keys, such as `kABAddressStreetKey`. Each attribute value contains the localized description of the key. (For example, the value of a Canadian `kABAddressZIPKey` field would be “Postal Code”, while the value of a French one would be “Code Postal”.)

To get the dictionary containing a street address for a person record, use [`value(forProperty:)`](abrecord-swift.class/value(forproperty:).md) with the property `kABAddressProperty`, and then getting one of the values from the multivalue that is returned.

## Parameters

- `address`: The dictionary containing a street address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/formattedaddress(from:))*