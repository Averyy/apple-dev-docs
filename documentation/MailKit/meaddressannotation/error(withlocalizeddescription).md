# error(withLocalizedDescription:)

**Framework**: MailKit  
**Kind**: method  
**Role**: Type Method

Indicates an address is invalid and may result in failure to deliver a message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func error(withLocalizedDescription localizedDescription: String) -> MEAddressAnnotation
```

```objc
+ (MEAddressAnnotation *) errorWithLocalizedDescription:(NSString *) localizedDescription;
```

## Return Value

An annotation that indicates an email address is invalid and may result in failure to deliver a message.

## Parameters

- `localizedDescription`: A user-visible string with details about the reason the address is invalid.

## See Also

### Specifying Email Address Validity
- [class func success(withLocalizedDescription: String) -> MEAddressAnnotation](./success%28withlocalizeddescription%29.md)
  Indicates an address is valid and correct.
- [class func warning(withLocalizedDescription: String) -> MEAddressAnnotation](./warning%28withlocalizeddescription%29.md)
  Indicates an address may be invalid or needs attention.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meaddressannotation/error(withlocalizeddescription:))*