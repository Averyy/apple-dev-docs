# sortOrder

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The sort order for contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sortOrder: CNContactSortOrder { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic) CNContactSortOrder sortOrder;
```

*macOS*

```objc
@property (atomic) CNContactSortOrder sortOrder;
```

## Discussion

The default sort order is `CNContactSortOrderNone`.

## See Also

### Configuring the Fetch Options
- [var mutableObjects: Bool](./mutableobjects.md)
  A Boolean value that indicates whether to return mutable contacts.
- [var unifyResults: Bool](./unifyresults.md)
  A Boolean value that indicates whether to return linked contacts as unified contacts.
- [enum CNContactSortOrder](../cncontactsortorder.md)
  Indicates the sorting order for contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/sortorder)*