---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcontactviewsynchronizerprotocol"
framework: "CareKit/CareKit"
---

# OCKContactViewSynchronizerProtocol

**Framework**: CareKit/CareKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that describes a view synchronizer for contacts.

## Declaration

```swift
protocol OCKContactViewSynchronizerProtocol : OCKAnyContactViewSynchronizerProtocol
```

## Topics

### Associated Types
- [associatedtype View : UIView, OCKContactDisplayable](./ockcontactviewsynchronizerprotocol/view.md)
  The type of the view that will be synchronized
### Instance Methods
- [func makeView() -> View](./ockcontactviewsynchronizerprotocol/makeview%28%29.md)
  Initialize a view to be synchronized.
- [func updateView(View, context: OCKSynchronizationContext<OCKAnyContact?>)](./ockcontactviewsynchronizerprotocol/updateview%28_,context%29.md)
  Update a view using the given context.

## Relationships

### Inherits From
- [OCKAnyContactViewSynchronizerProtocol](./ockanycontactviewsynchronizerprotocol.md)

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
- [protocol OCKAnyContactViewSynchronizerProtocol](./ockanycontactviewsynchronizerprotocol.md)
  A protocol that describes a type-erased view synchronizer for contacts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcontactviewsynchronizerprotocol)*