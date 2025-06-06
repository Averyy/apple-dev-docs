# versionIdentifiers

**Framework**: Core Data  
**Kind**: property

The set of developer-defined version identifiers for the object model.

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
var versionIdentifiers: Set<AnyHashable> { get set }
```

#### Discussion

Merged models return the combined collection of identifiers. The Core Data framework does not assign a default identifier to object models, nor does it depend on this value at runtime. For models you create in Xcode, set this value in the model inspector.

Use this value when debugging to help determine the models that Core Data merges to create the merged model.

## See Also

- [var versionChecksum: String](nsmanagedobjectmodel/versionchecksum.md)
  The Base64-encoded 128-bit model version hash.
- [var entityVersionHashesByName: [String : Data]](nsmanagedobjectmodel/entityversionhashesbyname.md)
  The dictionary of the model’s entity names and their corresponding version hashes.
- [func isConfiguration(withName: String?, compatibleWithStoreMetadata: [String : Any]) -> Bool](nsmanagedobjectmodel/isconfiguration(withname:compatiblewithstoremetadata:).md)
  Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/versionidentifiers)*