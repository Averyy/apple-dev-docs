# unifyResults

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to return linked contacts as unified contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var unifyResults: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic) BOOL unifyResults;
```

*macOS*

```objc
@property (atomic) BOOL unifyResults;
```

## Discussion

A unified contact is an aggregation of properties from a set of linked individual contacts. When the value of this property is [`true`](../../Swift/true.md), the fetch returns unified contacts; otherwise, it returns individual contacts. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Configuring the Fetch Options
- [var mutableObjects: Bool](./mutableobjects.md)
  A Boolean value that indicates whether to return mutable contacts.
- [var sortOrder: CNContactSortOrder](./sortorder.md)
  The sort order for contacts.
- [enum CNContactSortOrder](../cncontactsortorder.md)
  Indicates the sorting order for contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/unifyresults)*