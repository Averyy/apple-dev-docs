# cloudIdentifiers(forLocalIdentifiers:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Retrieves the equivalent iCloud identifiers for the list of local identifiers.

**Availability**:
- macOS 10.13+ - Deprecated in 12.0

> **Deprecated**: Use [`cloudIdentifierMappingsForLocalIdentifiers:`](./cloudidentifiermappingsforlocalidentifiers_.md) instead.

## Declaration

```swift
func cloudIdentifiers(forLocalIdentifiers localIdentifiers: [String]) -> [PHCloudIdentifier]
```

```objc
- (NSArray<PHCloudIdentifier *> *) cloudIdentifiersForLocalIdentifiers:(NSArray<NSString *> *) localIdentifiers;
```

#### Return Value

The array of corresponding iCloud identifiers.

#### Discussion

Retrieving iCloud identifiers can be an expensive operation, so you should perform this lookup sparingly. Instead, work with local identifiers and retrieve their iCloud identifier equivalents only once: either after loading from or before saving to persistent storage.

## Parameters

- `localIdentifiers`: The local identifiers for which to retrieve iCloud identifier equivalents.

## See Also

### Converting Between Local and iCloud Identifiers
- [func cloudIdentifierMappings(forLocalIdentifiers: [String]) -> [String : Result<PHCloudIdentifier, any Error>]](./cloudidentifiermappings%28forlocalidentifiers%29.md)
  Retrieves the cloud identifier mappings for the list of local identifiers.
- [func localIdentifierMappings(for: [PHCloudIdentifier]) -> [PHCloudIdentifier : Result<String, any Error>]](./localidentifiermappings%28for%29.md)
  Retrieves the local identifier mappings for the list of cloud identifiers.
- [class PHCloudIdentifier](../phcloudidentifier.md)
  An object that identifies an asset or collection that syncs through iCloud Photos.
- [func localIdentifiers(for: [PHCloudIdentifier]) -> [String]](./localidentifiers%28for%29.md)
  Retrieves the equivalent local identifiers for the list of iCloud identifiers.
- [let PHLocalIdentifierNotFound: String](../phlocalidentifiernotfound.md)
  A constant value that indicates that the system can’t resolve a local object from a global identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/cloudidentifiers(forlocalidentifiers:))*