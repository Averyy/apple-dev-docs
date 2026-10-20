# countryCode

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

An ISO country code.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var countryCode: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * countryCode;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * countryCode;
```

#### Discussion

ISO is the default country code for phone numbers. This is determined by the device’s SIM card or the operating system’s configured language.

## See Also

### Getting the Default Values
- [var sortOrder: CNContactSortOrder](./sortorder.md)
  Default sorting order by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactsuserdefaults/countrycode)*