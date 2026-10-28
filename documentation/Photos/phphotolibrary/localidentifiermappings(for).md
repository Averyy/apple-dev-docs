# localIdentifierMappings(for:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Retrieves the local identifier mappings for the list of cloud identifiers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
func localIdentifierMappings(for cloudIdentifiers: [PHCloudIdentifier]) -> [PHCloudIdentifier : Result<String, any Error>]
```

## Return Value

A dictionary that contains a map of cloud identifiers to their corresponding local mappings.

## Discussion

Retrieving local identifiers can be an expensive operation, so perform this lookup sparingly. Instead, work with local identifiers and perform mapping work at load and save points. Then store and share the cloud identifiers to make them available on other devices.

If the attempt to look up a local identifier fails, the error parameter indicates the reason.

## Parameters

- `cloudIdentifiers`: A list of cloud identifiers for which to retrieve local identifier mappings.

## See Also

### Converting Between Local and iCloud Identifiers
- [func cloudIdentifierMappings(forLocalIdentifiers: [String]) -> [String : Result<PHCloudIdentifier, any Error>]](./cloudidentifiermappings%28forlocalidentifiers%29.md)
  Retrieves the cloud identifier mappings for the list of local identifiers.
- [class PHCloudIdentifier](../phcloudidentifier.md)
  An object that identifies an asset or collection that syncs through iCloud Photos.
- [func cloudIdentifiers(forLocalIdentifiers: [String]) -> [PHCloudIdentifier]](./cloudidentifiers%28forlocalidentifiers%29.md)
  Retrieves the equivalent iCloud identifiers for the list of local identifiers.
- [func localIdentifiers(for: [PHCloudIdentifier]) -> [String]](./localidentifiers%28for%29.md)
  Retrieves the equivalent local identifiers for the list of iCloud identifiers.
- [let PHLocalIdentifierNotFound: String](../phlocalidentifiernotfound.md)
  A constant value that indicates that the system can’t resolve a local object from a global identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/localidentifiermappings(for:))*