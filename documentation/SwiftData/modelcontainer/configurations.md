# configurations

**Framework**: SwiftData  
**Kind**: property

The configurations that describe how to manage the persisted data for specific groups of models.

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
var configurations: Set<ModelConfiguration> { get set }
```

#### Discussion

Use this property to access or update the configurations that the container uses to manage model data. The default value is the set of configurations you specified when calling one of the container’s initializers.

> ❗ **Important**: A container must have at least one configuration. If you don’t specify any at initialization, the framework creates an instance of [`ModelConfiguration`](modelconfiguration.md) for you by combining your app’s entitlements with the type’s default values.

## See Also

- [let schema: Schema](modelcontainer/schema.md)
  The schema that maps your app’s model classes to the associated data in the app’s persistent storage.
- [let migrationPlan: (any SchemaMigrationPlan.Type)?](modelcontainer/migrationplan.md)
  The plan that describes the evolution of your app’s schema and how to migrate between specific versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontainer/configurations)*