# PHLocalIdentifierMapping

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An object that contains the local identifier result from looking up a cloud identifier, or an error indicating why the lookup failed.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@interface PHLocalIdentifierMapping : NSObject
```

## Topics

### Getting the Local Identifier
- [localIdentifier](./phlocalidentifiermapping/localidentifier.md)
  The local identifier associated with a iCloud identifier.
### Getting the Lookup Error Reason
- [error](./phlocalidentifiermapping/error.md)
  An error indicating why the local identifier lookup failed.

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
- [PHCloudIdentifierMapping](./phcloudidentifiermapping.md)
  An object that contains the cloud identifier result from looking up a local identifier, or an error indicating why the lookup failed.
- [func cloudIdentifiers(forLocalIdentifiers: [String]) -> [PHCloudIdentifier]](./phphotolibrary/cloudidentifiers%28forlocalidentifiers%29.md)
  Retrieves the equivalent iCloud identifiers for the list of local identifiers.
- [func localIdentifiers(for: [PHCloudIdentifier]) -> [String]](./phphotolibrary/localidentifiers%28for%29.md)
  Retrieves the equivalent local identifiers for the list of iCloud identifiers.
- [let PHLocalIdentifierNotFound: String](./phlocalidentifiernotfound.md)
  A constant value that indicates that the system can’t resolve a local object from a global identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlocalidentifiermapping)*