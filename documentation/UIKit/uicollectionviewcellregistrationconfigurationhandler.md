# UICollectionViewCellRegistrationConfigurationHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that handles the cell registration and configuration.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```c
typedef void (^)(__kindof UICollectionViewCell *, NSIndexPath *, id) UICollectionViewCellRegistrationConfigurationHandler;
```

#### Discussion

The closure takes the following parameters:

- **`cell`**: The [`UICollectionViewCell`](./uicollectionviewcell.md) or subclass instance to configure.
- **`indexPath`**: The [`IndexPath`](../Foundation/indexpath.md) of the cell to configure.
- **`item`**: The data item you provide in [`dequeueConfiguredReusableCellWithRegistration:forIndexPath:item:`](./uicollectionview/dequeueconfiguredreusablecellwithregistration_forindexpath_item_.md).

## See Also

### Creating a cell registration
- [+ registrationWithCellClass:configurationHandler:](./uicollectionviewcellregistration/registrationwithcellclass_configurationhandler_.md)
  Creates a cell registration with the specified registration handler.
- [+ registrationWithCellNib:configurationHandler:](./uicollectionviewcellregistration/registrationwithcellnib_configurationhandler_.md)
  Creates a cell registration with the specified registration handler and nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcellregistrationconfigurationhandler)*