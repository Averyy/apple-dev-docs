# descriptorForRequiredKeysForNameOrder

**Framework**: Contacts  
**Kind**: property  
**Role**: Type Property

Returns the required key descriptor for the display name order.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var descriptorForRequiredKeysForNameOrder: any CNKeyDescriptor { get }
```

```objc
@property (class, readonly) id<CNKeyDescriptor> descriptorForRequiredKeysForNameOrder;
```

## See Also

### Getting a descriptor
- [class func descriptorForRequiredKeys(for: CNContactFormatterStyle) -> any CNKeyDescriptor](./descriptorforrequiredkeys%28for%29.md)
  Returns the required key descriptor for the specified formatting style of the contact.
- [class var descriptorForRequiredKeysForDelimiter: any CNKeyDescriptor](./descriptorforrequiredkeysfordelimiter.md)
  Returns the required key descriptor for the name delimiter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/descriptorforrequiredkeysfornameorder)*