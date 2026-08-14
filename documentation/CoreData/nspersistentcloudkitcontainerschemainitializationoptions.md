# NSPersistentCloudKitContainerSchemaInitializationOptions

**Framework**: Core Data  
**Kind**: struct

Options that control the behavior when promoting the container’s schema to CloudKit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct NSPersistentCloudKitContainerSchemaInitializationOptions
```

## Topics

### Constants
- [static var dryRun: NSPersistentCloudKitContainerSchemaInitializationOptions](nspersistentcloudkitcontainerschemainitializationoptions/dryrun.md)
  A flag that indicates the container validates the model and generates the records, but doesn’t upload them to CloudKit.
- [static var printSchema: NSPersistentCloudKitContainerSchemaInitializationOptions](nspersistentcloudkitcontainerschemainitializationoptions/printschema.md)
  Prints the generated records to the console.
### Initializers
- [init(rawValue: UInt)](nspersistentcloudkitcontainerschemainitializationoptions/init(rawvalue:).md)
  Creates the schema initialization options using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func initializeCloudKitSchema(options: NSPersistentCloudKitContainerSchemaInitializationOptions) throws](nspersistentcloudkitcontainer/initializecloudkitschema(options:).md)
  Creates the CloudKit schema for all stores in the container that manage a CloudKit database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainerschemainitializationoptions)*