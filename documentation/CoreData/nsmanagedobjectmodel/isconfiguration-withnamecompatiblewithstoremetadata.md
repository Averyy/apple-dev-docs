# isConfiguration(withName:compatibleWithStoreMetadata:)

**Framework**: Core Data  
**Kind**: method

Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isConfiguration(withName configuration: String?, compatibleWithStoreMetadata metadata: [String : Any]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the configuration in the receiver specified by `configuration` is compatible with the store metadata given by `metadata`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method compares the version information in the store metadata with the entity versions of a given configuration. For information on specific differences, use [`entityVersionHashesByName`](nsmanagedobjectmodel/entityversionhashesbyname.md) and perform an entity-by-entity comparison.

## Parameters

- `configuration`: The name of a configuration in the receiver. Pass   to specify no configuration.
- `metadata`: Metadata for a persistent store.

## See Also

- [var versionChecksum: String](nsmanagedobjectmodel/versionchecksum.md)
  The Base64-encoded 128-bit model version hash.
- [var versionIdentifiers: Set<AnyHashable>](nsmanagedobjectmodel/versionidentifiers.md)
  The set of developer-defined version identifiers for the object model.
- [var entityVersionHashesByName: [String : Data]](nsmanagedobjectmodel/entityversionhashesbyname.md)
  The dictionary of the model’s entity names and their corresponding version hashes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/isconfiguration(withname:compatiblewithstoremetadata:))*