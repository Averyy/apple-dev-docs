# phoneticOrganizationName

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The phonetic name of the organization associated with the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var phoneticOrganizationName: String { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSString * phoneticOrganizationName;
```

*macOS*

```objc
@property (atomic, copy) NSString * phoneticOrganizationName;
```

#### Discussion

This property contains a string that specifies the pronunciation of the contact’s organization name.

## See Also

### Setting Work Information
- [var jobTitle: String](./jobtitle.md)
  The contact’s job title.
- [var departmentName: String](./departmentname.md)
  The name of the department associated with the contact.
- [var organizationName: String](./organizationname.md)
  The name of the organization associated with the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/phoneticorganizationname)*