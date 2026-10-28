# string(from:style:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Type Method

Returns a postal address as a string and formatted for the specified style.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func string(from postalAddress: CNPostalAddress, style: CNPostalAddressFormatterStyle) -> String
```

```objc
+ (NSString *) stringFromPostalAddress:(CNPostalAddress *) postalAddress style:(CNPostalAddressFormatterStyle) style;
```

## Return Value

The formatted postal address.

## Parameters

- `postalAddress`: The postal address to format.
- `style`: The postal formatting style to use. For a list of possible values, see [`CNPostalAddressFormatterStyle`](../cnpostaladdressformatterstyle.md).

## See Also

### Generating a formatted string
- [func string(from: CNPostalAddress) -> String](./string%28from%29.md)
  Returns a formatted postal address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnpostaladdressformatter/string(from:style:))*