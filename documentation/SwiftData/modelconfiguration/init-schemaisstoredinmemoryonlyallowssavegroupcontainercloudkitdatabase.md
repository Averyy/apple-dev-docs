# init(_:schema:isStoredInMemoryOnly:allowsSave:groupContainer:cloudKitDatabase:)

**Framework**: SwiftData  
**Kind**: init

Creates a named model configuration for the specified schema.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
init(_ name: String? = nil, schema: Schema? = nil, isStoredInMemoryOnly: Bool = false, allowsSave: Bool = true, groupContainer: ModelConfiguration.GroupContainer = .automatic, cloudKitDatabase: ModelConfiguration.CloudKitDatabase = .automatic)
```

## Parameters

- `name`: An optional name for the model configuration.
- `schema`: A schema that maps model classes to the associated data in the persistent storage. For more information, see [`Schema`](schema.md).
- `isStoredInMemoryOnly`: A Boolean value that determines whether the associated persistent storage is ephemeral and exists only in memory. The default value is `false`.
- `allowsSave`: A Boolean value that determines whether the associated persistent storage is writable. The default value is `true`.
- `groupContainer`: The option to use for detecting the configuration’s group container. For possible values, see [`ModelConfiguration.GroupContainer`](modelconfiguration/groupcontainer-swift.struct.md).
- `cloudKitDatabase`: The option to use for detecting the configuration’s CloudKit database. For possible values, see [`ModelConfiguration.CloudKitDatabase`](modelconfiguration/cloudkitdatabase-swift.struct.md).

## See Also

- [init(isStoredInMemoryOnly: Bool)](modelconfiguration/init(isstoredinmemoryonly:).md)
  Creates a basic model configuration.
- [init(for: any PersistentModel.Type..., isStoredInMemoryOnly: Bool)](modelconfiguration/init(for:isstoredinmemoryonly:).md)
  Creates a model configuration for the specified model types.
- [init(String?, schema: Schema?, url: URL, allowsSave: Bool, cloudKitDatabase: ModelConfiguration.CloudKitDatabase)](modelconfiguration/init(_:schema:url:allowssave:cloudkitdatabase:).md)
  Creates a named model configuration that specifies the on-disk location of the schema’s persistent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/init(_:schema:isstoredinmemoryonly:allowssave:groupcontainer:cloudkitdatabase:))*