# NSPersistentCloudKitContainerSchemaInitializationOptions

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Options that control the behavior when promoting the container’s schema to CloudKit.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct NSPersistentCloudKitContainerSchemaInitializationOptions
```

```c
enum NSPersistentCloudKitContainerSchemaInitializationOptions : NSUInteger;
```

## Topics

### Constants
- [static var dryRun: NSPersistentCloudKitContainerSchemaInitializationOptions](./nspersistentcloudkitcontainerschemainitializationoptions/dryrun.md)
  A flag that indicates the container validates the model and generates the records, but doesn’t upload them to CloudKit.
- [static var printSchema: NSPersistentCloudKitContainerSchemaInitializationOptions](./nspersistentcloudkitcontainerschemainitializationoptions/printschema.md)
  Prints the generated records to the console.
- [NSPersistentCloudKitContainerSchemaInitializationOptionsNone](./nspersistentcloudkitcontainerschemainitializationoptions/nspersistentcloudkitcontainerschemainitializationoptionsnone.md)
  Indicates there are no specified schema options.
### Initializers
- [init(rawValue: UInt)](./nspersistentcloudkitcontainerschemainitializationoptions/init%28rawvalue%29.md)
  Creates the schema initialization options using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Promoting Your Schema
- [func initializeCloudKitSchema(options: NSPersistentCloudKitContainerSchemaInitializationOptions) throws](./nspersistentcloudkitcontainer/initializecloudkitschema%28options%29.md)
  Creates the CloudKit schema for all stores in the container that manage a CloudKit database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainerschemainitializationoptions)*