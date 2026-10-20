# mutableObjects

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to return mutable contacts.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mutableObjects: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic) BOOL mutableObjects;
```

*macOS*

```objc
@property (atomic) BOOL mutableObjects;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the fetch returns [`CNMutableContact`](../cnmutablecontact.md) objects; otherwise it returns [`CNContact`](../cncontact.md) objects. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the Fetch Options
- [var unifyResults: Bool](./unifyresults.md)
  A Boolean value that indicates whether to return linked contacts as unified contacts.
- [var sortOrder: CNContactSortOrder](./sortorder.md)
  The sort order for contacts.
- [enum CNContactSortOrder](../cncontactsortorder.md)
  Indicates the sorting order for contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/mutableobjects)*