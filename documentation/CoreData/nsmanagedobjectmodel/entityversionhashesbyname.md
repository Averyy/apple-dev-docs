# entityVersionHashesByName

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The dictionary of the model’s entity names and their corresponding version hashes.

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
var entityVersionHashesByName: [String : Data] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,NSData *> * entityVersionHashesByName;
```

## Discussion

Core Data use the dictionary of version hash information is to determine schema compatibility.

## See Also

### Versioning and migrating entities
- [var versionChecksum: String](./versionchecksum.md)
  The Base64-encoded 128-bit model version hash.
- [var versionIdentifiers: Set<AnyHashable>](./versionidentifiers.md)
  The set of developer-defined version identifiers for the object model.
- [func isConfiguration(withName: String?, compatibleWithStoreMetadata: [String : Any]) -> Bool](./isconfiguration%28withname,compatiblewithstoremetadata%29.md)
  Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/entityversionhashesbyname)*