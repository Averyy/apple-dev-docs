---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcontactslistviewcontroller"
framework: "CareKit/CareKit"
---

# OCKContactsListViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that queries and displays contacts in a store.

## Declaration

```swift
@MainActor
class OCKContactsListViewController<ContactViewSynchronizer> where ContactViewSynchronizer : ViewSynchronizing, ContactViewSynchronizer.View : OCKContactDisplayable, ContactViewSynchronizer.ViewModel == (any OCKAnyContact)?
```

## Topics

### Initializers
- [init(store: OCKAnyStoreProtocol)](./ockcontactslistviewcontroller/init%28store%29.md)
  Creates a view controller that queries and displays contacts in a store.
- [init(store: OCKAnyStoreProtocol, contactViewSynchronizer: ContactViewSynchronizer)](./ockcontactslistviewcontroller/init%28store,contactviewsynchronizer%29.md)
  Creates a view controller that queries and displays contacts in a store.
### Instance Methods
- [func viewDidLoad()](./ockcontactslistviewcontroller/viewdidload%28%29.md)

## Relationships

### Inherits From
- [SynchronizedViewController](./synchronizedviewcontroller.md)
### Conforms To
- Foundation.NSCoding
- Foundation.NSExtensionRequestHandling
- ObjectiveC.NSObjectProtocol
- Swift.CVarArg
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype
- UIKit.UIActivityItemsConfigurationProviding
- UIKit.UIAppearanceContainer
- UIKit.UIContentContainer
- UIKit.UIFocusEnvironment
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIResponderStandardEditActions
- UIKit.UIStateRestoring
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring

## See Also

### Displaying contacts in UIKit
- [class OCKContactViewController](./ockcontactviewcontroller.md)
  A view controller that displays a contact view and keeps it synchronized with a store.
- [class OCKSimpleContactViewController](./ocksimplecontactviewcontroller.md)
  A view controller that displays a simple contact view and keeps it synchronized with a store.
- [class OCKDetailedContactViewController](./ockdetailedcontactviewcontroller.md)
  A view controller that displays a detailed contact view and keeps it synchronized with a store.
- [class OCKSimpleContactViewSynchronizer](./ocksimplecontactviewsynchronizer.md)
  A synchronizer that creates and updates a simple contact view.
- [class OCKDetailedContactViewSynchronizer](./ockdetailedcontactviewsynchronizer.md)
  A synchronizer that creates and updates a contact view.
- [protocol OCKContactViewSynchronizerProtocol](./ockcontactviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for contacts.
- [protocol OCKAnyContactViewSynchronizerProtocol](./ockanycontactviewsynchronizerprotocol.md)
  A protocol that describes a type-erased view synchronizer for contacts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcontactslistviewcontroller)*