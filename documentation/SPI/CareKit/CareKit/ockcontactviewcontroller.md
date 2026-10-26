---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcontactviewcontroller"
framework: "CareKit/CareKit"
---

# OCKContactViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that displays a contact view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
class OCKContactViewController<ViewSynchronizer> where ViewSynchronizer : ViewSynchronizing, ViewSynchronizer.View : OCKContactDisplayable, ViewSynchronizer.ViewModel == (any OCKAnyContact)?
```

## Topics

### Initializers
- [init(query: OCKContactQuery, store: OCKAnyStoreProtocol, viewSynchronizer: ViewSynchronizer)](./ockcontactviewcontroller/init%28query,store,viewsynchronizer%29.md)
  A view controller that displays a contact view and keeps it synchronized with a store.
### Instance Properties
- [var contactView: ViewSynchronizer.View](./ockcontactviewcontroller/contactview.md)
  The view that is being synchronized against the store.
### Instance Methods
- [func viewDidLoad()](./ockcontactviewcontroller/viewdidload%28%29.md)

## Relationships

### Inherits From
- [SynchronizedViewController](./synchronizedviewcontroller.md)
### Inherited By
- [OCKDetailedContactViewController](./ockdetailedcontactviewcontroller.md)
- [OCKSimpleContactViewController](./ocksimplecontactviewcontroller.md)
### Conforms To
- Foundation.NSCoding
- Foundation.NSExtensionRequestHandling
- ObjectiveC.NSObjectProtocol
- Swift.CVarArg
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
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
- [protocol OCKAnyContactViewSynchronizerProtocol](./ockanycontactviewsynchronizerprotocol.md)
  A protocol that describes a type-erased view synchronizer for contacts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcontactviewcontroller)*