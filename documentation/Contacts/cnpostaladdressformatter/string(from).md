# string(from:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Returns a formatted postal address.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func string(from postalAddress: CNPostalAddress) -> String
```

```objc
- (NSString *) stringFromPostalAddress:(CNPostalAddress *) postalAddress;
```

#### Return Value

The formatted postal address.

## Parameters

- `postalAddress`: The postal address to format.

## See Also

### Generating a formatted string
- [class func string(from: CNPostalAddress, style: CNPostalAddressFormatterStyle) -> String](./string%28from,style%29.md)
  Returns a postal address as a string and formatted for the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnpostaladdressformatter/string(from:))*