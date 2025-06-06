# predicate

**Framework**: Contacts  
**Kind**: property

The predicate to match contacts against.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var predicate: NSPredicate? { get set }
```

#### Discussion

Set the value of this property to `nil` to match all contacts or use the search predicates in [`CNContact`](cncontact.md). Compound predicates are not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/predicate)*