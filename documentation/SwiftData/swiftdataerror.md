# SwiftDataError

**Framework**: SwiftData  
**Kind**: struct

A type that describes a SwiftData error.

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
struct SwiftDataError
```

## Topics

### Fetch errors
- [static let includePendingChangesWithBatchSize: SwiftDataError](swiftdataerror/includependingchangeswithbatchsize.md)
- [static let sortingPendingChangesWithIdentifiers: SwiftDataError](swiftdataerror/sortingpendingchangeswithidentifiers.md)
- [static let unsupportedKeyPath: SwiftDataError](swiftdataerror/unsupportedkeypath.md)
- [static let unsupportedPredicate: SwiftDataError](swiftdataerror/unsupportedpredicate.md)
- [static let unsupportedSortDescriptor: SwiftDataError](swiftdataerror/unsupportedsortdescriptor.md)
### Configuration errors
- [static let configurationFileNameContainsInvalidCharacters: SwiftDataError](swiftdataerror/configurationfilenamecontainsinvalidcharacters.md)
- [static let configurationFileNameTooLong: SwiftDataError](swiftdataerror/configurationfilenametoolong.md)
- [static let configurationSchemaNotFoundInContainerSchema: SwiftDataError](swiftdataerror/configurationschemanotfoundincontainerschema.md)
- [static let duplicateConfiguration: SwiftDataError](swiftdataerror/duplicateconfiguration.md)
### Container errors
- [static let loadIssueModelContainer: SwiftDataError](swiftdataerror/loadissuemodelcontainer.md)
### Context errors
- [static let modelValidationFailure: SwiftDataError](swiftdataerror/modelvalidationfailure.md)
- [static let missingModelContext: SwiftDataError](swiftdataerror/missingmodelcontext.md)
### Migration errors
- [static let backwardMigration: SwiftDataError](swiftdataerror/backwardmigration.md)
- [static let unknownSchema: SwiftDataError](swiftdataerror/unknownschema.md)
### Operators
- [static func == (SwiftDataError, SwiftDataError) -> Bool](swiftdataerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func ~= (SwiftDataError, any Error) -> Bool](swiftdataerror/~=(_:_:).md)
### Instance Properties
- [var hashValue: Int](swiftdataerror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](swiftdataerror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let historyTokenExpired: SwiftDataError](swiftdataerror/historytokenexpired.md)
- [static let invalidTransactionFetchRequest: SwiftDataError](swiftdataerror/invalidtransactionfetchrequest.md)
### Default Implementations
- [Equatable Implementations](swiftdataerror/equatable-implementations.md)
- [Error Implementations](swiftdataerror/error-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/swiftdataerror)*