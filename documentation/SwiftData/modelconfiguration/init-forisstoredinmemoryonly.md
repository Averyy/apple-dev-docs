# init(for:isStoredInMemoryOnly:)

**Framework**: SwiftData  
**Kind**: init

Creates a model configuration for the specified model types.

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
init(for forTypes: any PersistentModel.Type..., isStoredInMemoryOnly: Bool = false)
```

## Parameters

- `forTypes`: A list of persistent model types.
- `isStoredInMemoryOnly`: A Boolean value that determines whether the   associated persistent storage is ephemeral and exists only in memory. The   default value is  .

## See Also

- [init(isStoredInMemoryOnly: Bool)](modelconfiguration/init(isstoredinmemoryonly:).md)
  Creates a basic model configuration.
- [init(String?, schema: Schema?, isStoredInMemoryOnly: Bool, allowsSave: Bool, groupContainer: ModelConfiguration.GroupContainer, cloudKitDatabase: ModelConfiguration.CloudKitDatabase)](modelconfiguration/init(_:schema:isstoredinmemoryonly:allowssave:groupcontainer:cloudkitdatabase:).md)
  Creates a named model configuration for the specified schema.
- [init(String?, schema: Schema?, url: URL, allowsSave: Bool, cloudKitDatabase: ModelConfiguration.CloudKitDatabase)](modelconfiguration/init(_:schema:url:allowssave:cloudkitdatabase:).md)
  Creates a named model configuration that specifies the on-disk location of the schema’s persistent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/init(for:isstoredinmemoryonly:))*