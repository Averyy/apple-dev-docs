# isConfiguration(withName:compatibleWithStoreMetadata:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isConfiguration(withName configuration: String?, compatibleWithStoreMetadata metadata: [String : Any]) -> Bool
```

```objc
- (BOOL) isConfiguration:(NSString *) configuration compatibleWithStoreMetadata:(NSDictionary<NSString *,id> *) metadata;
```

#### Return Value

[`true`](../../Swift/true.md) if the configuration in the receiver specified by `configuration` is compatible with the store metadata given by `metadata`, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method compares the version information in the store metadata with the entity versions of a given configuration. For information on specific differences, use [`entityVersionHashesByName`](./entityversionhashesbyname.md) and perform an entity-by-entity comparison.

## Parameters

- `configuration`: The name of a configuration in the receiver. Pass `nil` to specify no configuration.
- `metadata`: Metadata for a persistent store.

## See Also

### Versioning and migrating entities
- [var versionChecksum: String](./versionchecksum.md)
  The Base64-encoded 128-bit model version hash.
- [var versionIdentifiers: Set<AnyHashable>](./versionidentifiers.md)
  The set of developer-defined version identifiers for the object model.
- [var entityVersionHashesByName: [String : Data]](./entityversionhashesbyname.md)
  The dictionary of the model’s entity names and their corresponding version hashes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/isconfiguration(withname:compatiblewithstoremetadata:))*