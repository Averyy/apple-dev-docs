# unknownDataStoreSchema

**Framework**: SwiftData  
**Kind**: property

An error that indicates the data store’s schema is not recognized.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Swift 5.9+

## Declaration

```swift
static let unknownDataStoreSchema: SwiftDataError
```

#### Discussion

This error occurs when a `ModelContainer` attempts to load a data store whose schema does not match the current schema or any schema defined in the provided migration plan.

When you encounter this error, the data store likely contains data from a schema version that your app no longer supports. To resolve this:

- Add the missing schema version to your `SchemaMigrationPlan`
- Provide a custom migration stage to handle the unrecognized schema
- Consider whether the data store should be recreated

This error is only thrown on processes linked on or after macOS 27 / iOS 27. On earlier versions, `loadIssueModelContainer` is thrown instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/swiftdataerror/unknowndatastoreschema)*