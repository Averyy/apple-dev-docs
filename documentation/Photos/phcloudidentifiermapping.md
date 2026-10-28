# PHCloudIdentifierMapping

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An object that contains the cloud identifier result from looking up a local identifier, or an error indicating why the lookup failed.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@interface PHCloudIdentifierMapping : NSObject
```

## Overview

The error property exhibits two common errors—[`PHPhotosError.Code.identifierNotFound`](./phphotoserror-swift.struct/code/identifiernotfound.md) and [`PHPhotosError.Code.multipleIdentifiersFound`](./phphotoserror-swift.struct/code/multipleidentifiersfound.md). When encountering multiple identifiers, use the error’s [`userInfo`](../Foundation/nserror/userinfo.md) property to retrieve a list of matched local identifiers. You can access them using [`PHLocalIdentifiersErrorKey`](./phlocalidentifierserrorkey.md).

## Topics

### Getting the Cloud Identifier
- [cloudIdentifier](./phcloudidentifiermapping/cloudidentifier.md)
  The iCloud identifier associated with the local identifier.
### Getting the Lookup Error Reason
- [error](./phcloudidentifiermapping/error.md)
  An error indicating why the iCloud identifier lookup failed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Converting Between Local and iCloud Identifiers
- [- cloudIdentifierMappingsForLocalIdentifiers:](./phphotolibrary/cloudidentifiermappingsforlocalidentifiers_.md)
  Retrieves the cloud identifier mappings for the list of local identifiers.
- [- localIdentifierMappingsForCloudIdentifiers:](./phphotolibrary/localidentifiermappingsforcloudidentifiers_.md)
  Retrieves the local identifier mappings for the list of cloud identifiers.
- [class PHCloudIdentifier](./phcloudidentifier.md)
  An object that identifies an asset or collection that syncs through iCloud Photos.
- [PHLocalIdentifierMapping](./phlocalidentifiermapping.md)
  An object that contains the local identifier result from looking up a cloud identifier, or an error indicating why the lookup failed.
- [func cloudIdentifiers(forLocalIdentifiers: [String]) -> [PHCloudIdentifier]](./phphotolibrary/cloudidentifiers%28forlocalidentifiers%29.md)
  Retrieves the equivalent iCloud identifiers for the list of local identifiers.
- [func localIdentifiers(for: [PHCloudIdentifier]) -> [String]](./phphotolibrary/localidentifiers%28for%29.md)
  Retrieves the equivalent local identifiers for the list of iCloud identifiers.
- [let PHLocalIdentifierNotFound: String](./phlocalidentifiernotfound.md)
  A constant value that indicates that the system can’t resolve a local object from a global identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcloudidentifiermapping)*