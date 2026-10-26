# UICollectionViewSupplementaryRegistrationConfigurationHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A block that handles the supplementary view registration and configuration.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```c
typedef void (^)(__kindof UICollectionReusableView *, NSString *, NSIndexPath *) UICollectionViewSupplementaryRegistrationConfigurationHandler;
```

## See Also

### Creating a supplementary registration
- [+ registrationWithSupplementaryClass:elementKind:configurationHandler:](./uicollectionviewsupplementaryregistration/registrationwithsupplementaryclass_elementkind_configurationhandler_.md)
  Creates a supplementary registration for the specified element kind with a registration handler.
- [+ registrationWithSupplementaryNib:elementKind:configurationHandler:](./uicollectionviewsupplementaryregistration/registrationwithsupplementarynib_elementkind_configurationhandler_.md)
  Creates a supplementary registration for the specified element kind with a registration handler and nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewsupplementaryregistrationconfigurationhandler)*