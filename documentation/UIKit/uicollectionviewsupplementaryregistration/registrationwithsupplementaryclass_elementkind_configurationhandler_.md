# registrationWithSupplementaryClass:elementKind:configurationHandler:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a supplementary registration for the specified element kind with a registration handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) registrationWithSupplementaryClass:(Class) supplementaryClass elementKind:(NSString *) elementKind configurationHandler:(UICollectionViewSupplementaryRegistrationConfigurationHandler) configurationHandler;
```

## See Also

### Creating a supplementary registration
- [+ registrationWithSupplementaryNib:elementKind:configurationHandler:](./registrationwithsupplementarynib_elementkind_configurationhandler_.md)
  Creates a supplementary registration for the specified element kind with a registration handler and nib file.
- [UICollectionViewSupplementaryRegistrationConfigurationHandler](../uicollectionviewsupplementaryregistrationconfigurationhandler.md)
  A block that handles the supplementary view registration and configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewsupplementaryregistration/registrationwithsupplementaryclass:elementkind:configurationhandler:)*