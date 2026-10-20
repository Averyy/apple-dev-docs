# phoneticOrganizationName

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The phonetic name of the organization associated with the contact.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var phoneticOrganizationName: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * phoneticOrganizationName;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * phoneticOrganizationName;
```

#### Discussion

This property contains a string that specifies the pronunciation of the contact’s organization name.

## See Also

### Getting Work Information
- [var jobTitle: String](./jobtitle.md)
  The contact’s job title.
- [var departmentName: String](./departmentname.md)
  The name of the department associated with the contact.
- [var organizationName: String](./organizationname.md)
  The name of the organization associated with the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/phoneticorganizationname)*