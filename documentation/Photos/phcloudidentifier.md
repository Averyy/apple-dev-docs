# PHCloudIdentifier

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An object that identifies an asset or collection that syncs through iCloud Photos.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.13+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class PHCloudIdentifier
```

```objc
@interface PHCloudIdentifier : NSObject
```

#### Overview

A cloud identifier is a type of identifier that behaves like a local identifier. Use cloud identifiers to identify objects that sync across devices through iCloud Photos. You can store, sync, and use cloud identifiers with devices synced with an iCloud account. You’re also able to use secure coding to encode and decode cloud identifiers.

A local identifier is valid for referring to objects only in the context of a local device. These objects include [`PHAsset`](./phasset.md), [`PHAssetCollection`](./phassetcollection.md), and [`PHCollectionList`](./phcollectionlist.md).

Because a cloud identifier is universal, you can use it on any iCloud-synced device. Convert the cloud identifier back to a local identifier and perform a fetch to find the equivalent object on that device. Perform batch lookups of identifiers using [`localIdentifierMappingsForCloudIdentifiers:`](./phphotolibrary/localidentifiermappingsforcloudidentifiers_.md) and [`cloudIdentifierMappingsForLocalIdentifiers:`](./phphotolibrary/cloudidentifiermappingsforlocalidentifiers_.md).

```swift
// Get the local identifier mappings for the cloud identifiers.
let identifierMappings = library.localIdentifierMappings(for: assetCloudIdentifiers)
```

Retrieving identifier mappings can be an expensive operation, so perform lookups sparingly. If a lookup fails, inspect the error property on [`PHCloudIdentifierMapping`](./phcloudidentifiermapping.md) or [`PHLocalIdentifierMapping`](./phlocalidentifiermapping.md) for details. See [`PHPhotosError.Code`](./phphotoserror-swift.struct/code.md) for additional error details.

```swift
// Iterate over the cloud identifiers and add or handle missing local identifiers.
for cloudIdentifier in assetCloudIdentifiers {
    guard let identifierMapping = identifierMappings[cloudIdentifier] else {
        print("Failed to find a mapping for \(cloudIdentifier).")
        continue
    }

    // Track the local identifier if it exists.
    if let localIdentifier = identifierMapping.localIdentifier {
        localIdentifiers.append(localIdentifier)
    } else if let error = identifierMapping.error as? PHPhotosError {
        switch error.code {
        case .identifierNotFound:
            // Skip the missing or deleted assets.
            print("Failed to find the local identifier for \(cloudIdentifier). \(error.localizedDescription))")
        case .multipleIdentifiersFound:
            // Prompt the user to resolve the cloud identifier that matched multiple assets.
            print("Found multiple local identifiers for \(cloudIdentifier). \(error.localizedDescription)")
            if let selectedLocalIdentifier = promptUserForPotentialReplacement(with: error.userInfo[PHLocalIdentifiersErrorKey]) {
                localIdentifiers.append(selectedLocalIdentifier)
            }
        default:
            print("Encountered an unexpected error looking up the local identifier for \(cloudIdentifier). \(error.localizedDescription)")
        }
    }
}

// Fetch assets using the found identifiers.
let mappedAssets = PHAsset.fetchAssets(withLocalIdentifiers: localIdentifiers, 
                                       options: nil)
```

## Topics

### Using Cloud Identifiers
- [init(stringValue: String)](./phcloudidentifier/init%28stringvalue%29.md)
  Deserializes a cloud identifier from its string value.
- [var stringValue: String](./phcloudidentifier/stringvalue.md)
  A string version of the cloud identifier to use in serialization.
- [class var notFound: PHCloudIdentifier](./phcloudidentifier/notfound.md)
  The global identifier used in an array slot for items that couldn’t be found.
### Initializers
- [init?(archivalStringValue: String)](./phcloudidentifier/init%28archivalstringvalue%29.md)
  Archival string can be used to serialize and deserialize the PHCloudIdentifier (Note the archival format is compatible with strings archived via the deprecated API `stringValue`)
- [init?(coder: NSCoder)](./phcloudidentifier/init%28coder%29.md)
### Instance Properties
- [var archivalStringValue: String](./phcloudidentifier/archivalstringvalue.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Converting Between Local and iCloud Identifiers
- [func cloudIdentifierMappings(forLocalIdentifiers: [String]) -> [String : Result<PHCloudIdentifier, any Error>]](./phphotolibrary/cloudidentifiermappings%28forlocalidentifiers%29.md)
  Retrieves the cloud identifier mappings for the list of local identifiers.
- [func localIdentifierMappings(for: [PHCloudIdentifier]) -> [PHCloudIdentifier : Result<String, any Error>]](./phphotolibrary/localidentifiermappings%28for%29.md)
  Retrieves the local identifier mappings for the list of cloud identifiers.
- [func cloudIdentifiers(forLocalIdentifiers: [String]) -> [PHCloudIdentifier]](./phphotolibrary/cloudidentifiers%28forlocalidentifiers%29.md)
  Retrieves the equivalent iCloud identifiers for the list of local identifiers.
- [func localIdentifiers(for: [PHCloudIdentifier]) -> [String]](./phphotolibrary/localidentifiers%28for%29.md)
  Retrieves the equivalent local identifiers for the list of iCloud identifiers.
- [let PHLocalIdentifierNotFound: String](./phlocalidentifiernotfound.md)
  A constant value that indicates that the system can’t resolve a local object from a global identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcloudidentifier)*