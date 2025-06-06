# migrationPlan

**Framework**: SwiftData  
**Kind**: property

The plan that describes the evolution of your app’s schema and how to migrate between specific versions.

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
final let migrationPlan: (any SchemaMigrationPlan.Type)?
```

#### Discussion

This property provides a reference to the migration plan you specified when calling one the container’s initializers. If you didn’t specify one, the property’s value is `nil`.

## See Also

- [let schema: Schema](modelcontainer/schema.md)
  The schema that maps your app’s model classes to the associated data in the app’s persistent storage.
- [var configurations: Set<ModelConfiguration>](modelcontainer/configurations.md)
  The configurations that describe how to manage the persisted data for specific groups of models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontainer/migrationplan)*