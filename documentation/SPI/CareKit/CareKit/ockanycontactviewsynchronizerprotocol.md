---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockanycontactviewsynchronizerprotocol"
framework: "CareKit/CareKit"
---

# OCKAnyContactViewSynchronizerProtocol

**Framework**: CareKit/CareKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that describes a type-erased view synchronizer for contacts.

## Declaration

```swift
protocol OCKAnyContactViewSynchronizerProtocol
```

## Topics

### Instance Methods
- [func makeAnyView() -> UIView & OCKContactDisplayable](./ockanycontactviewsynchronizerprotocol/makeanyview%28%29.md)
  Initialize a view to be synchronized.
- [func updateAnyView(UIView & OCKContactDisplayable, context: OCKSynchronizationContext<OCKAnyContact?>)](./ockanycontactviewsynchronizerprotocol/updateanyview%28_,context%29.md)
  Update a view using the given context

## Relationships

### Inherited By
- [OCKContactViewSynchronizerProtocol](./ockcontactviewsynchronizerprotocol.md)

## See Also

### Displaying contacts in UIKit
- [class OCKContactViewController](./ockcontactviewcontroller.md)
  A view controller that displays a contact view and keeps it synchronized with a store.
- [class OCKSimpleContactViewController](./ocksimplecontactviewcontroller.md)
  A view controller that displays a simple contact view and keeps it synchronized with a store.
- [class OCKDetailedContactViewController](./ockdetailedcontactviewcontroller.md)
  A view controller that displays a detailed contact view and keeps it synchronized with a store.
- [class OCKContactsListViewController](./ockcontactslistviewcontroller.md)
  A view controller that queries and displays contacts in a store.
- [class OCKSimpleContactViewSynchronizer](./ocksimplecontactviewsynchronizer.md)
  A synchronizer that creates and updates a simple contact view.
- [class OCKDetailedContactViewSynchronizer](./ockdetailedcontactviewsynchronizer.md)
  A synchronizer that creates and updates a contact view.
- [protocol OCKContactViewSynchronizerProtocol](./ockcontactviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for contacts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockanycontactviewsynchronizerprotocol)*