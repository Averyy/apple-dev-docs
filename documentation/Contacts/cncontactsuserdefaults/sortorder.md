# sortOrder

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

Default sorting order by name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sortOrder: CNContactSortOrder { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, readonly) CNContactSortOrder sortOrder;
```

*macOS*

```objc
@property (atomic, readonly) CNContactSortOrder sortOrder;
```

## Discussion

Sort order is determined by the operating system’s configured language or overridden by the user.

## See Also

### Getting the Default Values
- [var countryCode: String](./countrycode.md)
  An ISO country code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactsuserdefaults/sortorder)*