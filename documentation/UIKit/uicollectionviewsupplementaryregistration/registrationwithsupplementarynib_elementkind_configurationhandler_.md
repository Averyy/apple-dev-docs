# registrationWithSupplementaryNib:elementKind:configurationHandler:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a supplementary registration for the specified element kind with a registration handler and nib file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```objc
+ (instancetype) registrationWithSupplementaryNib:(UINib *) supplementaryNib elementKind:(NSString *) elementKind configurationHandler:(UICollectionViewSupplementaryRegistrationConfigurationHandler) configurationHandler;
```

## See Also

### Creating a supplementary registration
- [+ registrationWithSupplementaryClass:elementKind:configurationHandler:](./registrationwithsupplementaryclass_elementkind_configurationhandler_.md)
  Creates a supplementary registration for the specified element kind with a registration handler.
- [UICollectionViewSupplementaryRegistrationConfigurationHandler](../uicollectionviewsupplementaryregistrationconfigurationhandler.md)
  A block that handles the supplementary view registration and configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewsupplementaryregistration/registrationwithsupplementarynib:elementkind:configurationhandler:)*