# cloudIdentifierMappingsForLocalIdentifiers:

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Retrieves the cloud identifier mappings for the list of local identifiers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
- (NSDictionary<NSString *,PHCloudIdentifierMapping *> *) cloudIdentifierMappingsForLocalIdentifiers:(NSArray<NSString *> *) localIdentifiers;
```

#### Return Value

A dictionary that contains a map of local identifiers to their corresponding cloud mappings.

#### Discussion

Retrieving cloud identifiers can be an expensive operation, so perform this lookup sparingly. Instead, work with local identifiers and perform mapping work at load and save points. Then store and share the cloud identifiers to make them available on other devices.

If the attempt to look up a cloud identifier fails, the error parameter indicates the reason.

## Parameters

- `localIdentifiers`: A list of local identifiers for which to retrieve cloud identifiers mappings.

## See Also

### Converting Between Local and iCloud Identifiers
- [- localIdentifierMappingsForCloudIdentifiers:](./localidentifiermappingsforcloudidentifiers_.md)
  Retrieves the local identifier mappings for the list of cloud identifiers.
- [class PHCloudIdentifier](../phcloudidentifier.md)
  An object that identifies an asset or collection that syncs through iCloud Photos.
- [PHCloudIdentifierMapping](../phcloudidentifiermapping.md)
  An object that contains the cloud identifier result from looking up a local identifier, or an error indicating why the lookup failed.
- [PHLocalIdentifierMapping](../phlocalidentifiermapping.md)
  An object that contains the local identifier result from looking up a cloud identifier, or an error indicating why the lookup failed.
- [func cloudIdentifiers(forLocalIdentifiers: [String]) -> [PHCloudIdentifier]](./cloudidentifiers%28forlocalidentifiers%29.md)
  Retrieves the equivalent iCloud identifiers for the list of local identifiers.
- [func localIdentifiers(for: [PHCloudIdentifier]) -> [String]](./localidentifiers%28for%29.md)
  Retrieves the equivalent local identifiers for the list of iCloud identifiers.
- [let PHLocalIdentifierNotFound: String](../phlocalidentifiernotfound.md)
  A constant value that indicates that the system can’t resolve a local object from a global identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/cloudidentifiermappingsforlocalidentifiers:)*