# localIdentifiers(for:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Retrieves the equivalent local identifiers for the list of iCloud identifiers.

**Availability**:
- macOS 10.13+ - Deprecated in 12.0

> **Deprecated**: Use [`localIdentifierMappingsForCloudIdentifiers:`](./localidentifiermappingsforcloudidentifiers_.md) instead.

## Declaration

```swift
func localIdentifiers(for cloudIdentifiers: [PHCloudIdentifier]) -> [String]
```

```objc
- (NSArray<NSString *> *) localIdentifiersForCloudIdentifiers:(NSArray<PHCloudIdentifier *> *) cloudIdentifiers;
```

#### Return Value

The array of corresponding iCloud identifiers.

## Parameters

- `cloudIdentifiers`: The iCloud identifiers for which to retrieve local identifier equivalents.

## See Also

### Converting Between Local and iCloud Identifiers
- [func cloudIdentifierMappings(forLocalIdentifiers: [String]) -> [String : Result<PHCloudIdentifier, any Error>]](./cloudidentifiermappings%28forlocalidentifiers%29.md)
  Retrieves the cloud identifier mappings for the list of local identifiers.
- [func localIdentifierMappings(for: [PHCloudIdentifier]) -> [PHCloudIdentifier : Result<String, any Error>]](./localidentifiermappings%28for%29.md)
  Retrieves the local identifier mappings for the list of cloud identifiers.
- [class PHCloudIdentifier](../phcloudidentifier.md)
  An object that identifies an asset or collection that syncs through iCloud Photos.
- [func cloudIdentifiers(forLocalIdentifiers: [String]) -> [PHCloudIdentifier]](./cloudidentifiers%28forlocalidentifiers%29.md)
  Retrieves the equivalent iCloud identifiers for the list of local identifiers.
- [let PHLocalIdentifierNotFound: String](../phlocalidentifiernotfound.md)
  A constant value that indicates that the system can’t resolve a local object from a global identifier.
- [- cloudIdentifierMappingsForLocalIdentifiers:](./cloudidentifiermappingsforlocalidentifiers_.md)
  Retrieves the cloud identifier mappings for the list of local identifiers.
- [- localIdentifierMappingsForCloudIdentifiers:](./localidentifiermappingsforcloudidentifiers_.md)
  Retrieves the local identifier mappings for the list of cloud identifiers.
- [PHCloudIdentifierMapping](../phcloudidentifiermapping.md)
  An object that contains the cloud identifier result from looking up a local identifier, or an error indicating why the lookup failed.
- [PHLocalIdentifierMapping](../phlocalidentifiermapping.md)
  An object that contains the local identifier result from looking up a cloud identifier, or an error indicating why the lookup failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/localidentifiers(for:))*