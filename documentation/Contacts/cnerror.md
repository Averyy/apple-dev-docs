# CNError

**Framework**: Contacts  
**Kind**: struct

Error information that may be returned when using the methods of the Contacts framework.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CNError
```

## Topics

### Error codes
- [static var authorizationDenied: CNError.Code](cnerror/authorizationdenied.md)
  An error that indicates the system denied authorization.
- [static var changeHistoryExpired: CNError.Code](cnerror/changehistoryexpired.md)
  An error that indicates the change history expired.
- [static var changeHistoryInvalidAnchor: CNError.Code](cnerror/changehistoryinvalidanchor.md)
  An error that indicates a change history anchor is invalid.
- [static var changeHistoryInvalidFetchRequest: CNError.Code](cnerror/changehistoryinvalidfetchrequest.md)
  An error that indicates a change history fetch request is invalid.
- [static var clientIdentifierCollision: CNError.Code](cnerror/clientidentifiercollision.md)
  An error that indicates a client identifier collision.
- [static var clientIdentifierDoesNotExist: CNError.Code](cnerror/clientidentifierdoesnotexist.md)
  An error that indicates the client identifier doesn’t exist.
- [static var clientIdentifierInvalid: CNError.Code](cnerror/clientidentifierinvalid.md)
  An error that indicates the client identifier is invalid.
- [static var communicationError: CNError.Code](cnerror/communicationerror.md)
  An error that indicates a communication error occurred.
- [static var containmentCycle: CNError.Code](cnerror/containmentcycle.md)
  An error with the containment cycle.
- [static var containmentScope: CNError.Code](cnerror/containmentscope.md)
  An error with containment scope.
- [static var dataAccessError: CNError.Code](cnerror/dataaccesserror.md)
  An error with data access.
- [static var featureDisabledByUser: CNError.Code](cnerror/featuredisabledbyuser.md)
  An error that indicates the user disabled the feature.
- [static var featureNotAvailable: CNError.Code](cnerror/featurenotavailable.md)
  An error that indicates the feature isn’t available.
- [static var insertedRecordAlreadyExists: CNError.Code](cnerror/insertedrecordalreadyexists.md)
  An error that indicates the inserted record already exists.
- [static var noAccessableWritableContainers: CNError.Code](cnerror/noaccessablewritablecontainers.md)
  An error that indicates there are no accessible writable containers.
- [static var parentContainerNotWritable: CNError.Code](cnerror/parentcontainernotwritable.md)
  An error that indicates the parent container isn’t writable.
- [static var parentRecordDoesNotExist: CNError.Code](cnerror/parentrecorddoesnotexist.md)
  An error that indicates the parent record doesn’t exist.
- [static var policyViolation: CNError.Code](cnerror/policyviolation.md)
  An error that indicates a policy violation.
- [static var predicateInvalid: CNError.Code](cnerror/predicateinvalid.md)
  An error that indicates an invalid predicate.
- [static var recordDoesNotExist: CNError.Code](cnerror/recorddoesnotexist.md)
  An error that indicates a record doesn’t exist.
- [static var recordIdentifierInvalid: CNError.Code](cnerror/recordidentifierinvalid.md)
  An error that indicates a record identifier is invalid.
- [static var recordNotWritable: CNError.Code](cnerror/recordnotwritable.md)
  An error that indicates a record isn’t writable.
- [static var unauthorizedKeys: CNError.Code](cnerror/unauthorizedkeys.md)
  An error that indicates unauthorized keys usage.
- [static var vCardMalformed: CNError.Code](cnerror/vcardmalformed.md)
  An error that indicates a malformed vCard.
- [static var vCardSummarizationError: CNError.Code](cnerror/vcardsummarizationerror.md)
  An error that indicates a vCard summarization problem.
- [static var validationConfigurationError: CNError.Code](cnerror/validationconfigurationerror.md)
  An error with validation configuration.
- [static var validationMultipleErrors: CNError.Code](cnerror/validationmultipleerrors.md)
  An error that indicates the system encountered multiple validation errors.
- [static var validationTypeMismatch: CNError.Code](cnerror/validationtypemismatch.md)
  A validation error that indicates a type mismatch.
### Error details
- [var affectedRecordIdentifiers: [String]?](cnerror/affectedrecordidentifiers.md)
  An array of strings that uniquely identify the records affected by the error.
- [var affectedRecords: [AnyObject]?](cnerror/affectedrecords.md)
  An array of record objects for which the error applies.
- [CNError.Code](cnerror/code.md)
  Error codes that the system may return when you use Contacts framework methods.
- [var keyPaths: [String]?](cnerror/keypaths.md)
  An array of key paths associated with the error.
### Type Properties
- [static var errorDomain: String](cnerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [CNError.Code](cnerror/code.md)
  Error codes that the system may return when you use Contacts framework methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnerror)*