# CNError.Code

**Framework**: Contacts  
**Kind**: enum

Error codes that the system may return when you use Contacts framework methods.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Code
```

## Topics

### Errors
- [CNError.Code.authorizationDenied](cnerror/code/authorizationdenied.md)
  An error that indicates the system denied authorization.
- [CNError.Code.changeHistoryExpired](cnerror/code/changehistoryexpired.md)
  An error that indicates the change history expired.
- [CNError.Code.changeHistoryInvalidAnchor](cnerror/code/changehistoryinvalidanchor.md)
  An error that indicates a change history anchor is invalid.
- [CNError.Code.changeHistoryInvalidFetchRequest](cnerror/code/changehistoryinvalidfetchrequest.md)
  An error that indicates a change history fetch request is invalid.
- [CNError.Code.clientIdentifierCollision](cnerror/code/clientidentifiercollision.md)
  An error that indicates a client identifier collision.
- [CNError.Code.clientIdentifierInvalid](cnerror/code/clientidentifierinvalid.md)
  An error that indicates the client identifier is invalid.
- [CNError.Code.clientIdentifierDoesNotExist](cnerror/code/clientidentifierdoesnotexist.md)
  An error that indicates the client identifier doesn’t exist.
- [CNError.Code.communicationError](cnerror/code/communicationerror.md)
  An error that indicates a communication error occurred.
- [CNError.Code.containmentCycle](cnerror/code/containmentcycle.md)
  An error with the containment cycle.
- [CNError.Code.containmentScope](cnerror/code/containmentscope.md)
  An error with containment scope.
- [CNError.Code.dataAccessError](cnerror/code/dataaccesserror.md)
  An error with data access.
- [CNError.Code.featureDisabledByUser](cnerror/code/featuredisabledbyuser.md)
  An error that indicates the user disabled the feature.
- [CNError.Code.featureNotAvailable](cnerror/code/featurenotavailable.md)
  An error that indicates the feature isn’t available.
- [CNError.Code.insertedRecordAlreadyExists](cnerror/code/insertedrecordalreadyexists.md)
  An error that indicates the inserted record already exists.
- [CNError.Code.noAccessableWritableContainers](cnerror/code/noaccessablewritablecontainers.md)
  An error that indicates there are no accessible writable containers.
- [CNError.Code.parentContainerNotWritable](cnerror/code/parentcontainernotwritable.md)
  An error that indicates the parent container isn’t writable.
- [CNError.Code.parentRecordDoesNotExist](cnerror/code/parentrecorddoesnotexist.md)
  An error that indicates the parent record doesn’t exist.
- [CNError.Code.policyViolation](cnerror/code/policyviolation.md)
  An error that indicates a policy violation.
- [CNError.Code.predicateInvalid](cnerror/code/predicateinvalid.md)
  An error that indicates an invalid predicate.
- [CNError.Code.recordDoesNotExist](cnerror/code/recorddoesnotexist.md)
  An error that indicates a record doesn’t exist.
- [CNError.Code.recordIdentifierInvalid](cnerror/code/recordidentifierinvalid.md)
  An error that indicates a record identifier is invalid.
- [CNError.Code.recordNotWritable](cnerror/code/recordnotwritable.md)
  An error that indicates a record isn’t writable.
- [CNError.Code.unauthorizedKeys](cnerror/code/unauthorizedkeys.md)
  An error that indicates unauthorized keys usage.
- [CNError.Code.validationMultipleErrors](cnerror/code/validationmultipleerrors.md)
  An error that indicates the system encountered multiple validation errors.
- [CNError.Code.validationTypeMismatch](cnerror/code/validationtypemismatch.md)
  A validation error that indicates a type mismatch.
- [CNError.Code.validationConfigurationError](cnerror/code/validationconfigurationerror.md)
  An error with validation configuration.
- [CNError.Code.vCardMalformed](cnerror/code/vcardmalformed.md)
  An error that indicates a malformed vCard.
- [CNError.Code.vCardSummarizationError](cnerror/code/vcardsummarizationerror.md)
  An error that indicates a vCard summarization problem.
### Initializers
- [init?(rawValue: Int)](cnerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CNError](cnerror.md)
  Error information that may be returned when using the methods of the Contacts framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnerror/code)*