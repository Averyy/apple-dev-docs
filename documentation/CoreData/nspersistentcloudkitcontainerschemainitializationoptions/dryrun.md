# dryRun

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

A flag that indicates the container validates the model and generates the records, but doesn’t upload them to CloudKit.

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
static var dryRun: NSPersistentCloudKitContainerSchemaInitializationOptions { get }
```

```c
NSPersistentCloudKitContainerSchemaInitializationOptionsDryRun
```

#### Discussion

This option is useful for unit testing to ensure your managed object model is valid for use with CloudKit.

## See Also

### Constants
- [static var printSchema: NSPersistentCloudKitContainerSchemaInitializationOptions](./printschema.md)
  Prints the generated records to the console.
- [NSPersistentCloudKitContainerSchemaInitializationOptionsNone](./nspersistentcloudkitcontainerschemainitializationoptionsnone.md)
  Indicates there are no specified schema options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainerschemainitializationoptions/dryrun)*