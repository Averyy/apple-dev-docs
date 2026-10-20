# CNError.Code

**Framework**: Contacts  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CNErrorCode : NSInteger;
```

## Topics

### Errors
- [CNError.Code.authorizationDenied](./code/authorizationdenied.md)
  An error that indicates the system denied authorization.
- [CNError.Code.changeHistoryExpired](./code/changehistoryexpired.md)
  An error that indicates the change history expired.
- [CNError.Code.changeHistoryInvalidAnchor](./code/changehistoryinvalidanchor.md)
  An error that indicates a change history anchor is invalid.
- [CNError.Code.changeHistoryInvalidFetchRequest](./code/changehistoryinvalidfetchrequest.md)
  An error that indicates a change history fetch request is invalid.
- [CNError.Code.clientIdentifierCollision](./code/clientidentifiercollision.md)
  An error that indicates a client identifier collision.
- [CNError.Code.clientIdentifierInvalid](./code/clientidentifierinvalid.md)
  An error that indicates the client identifier is invalid.
- [CNError.Code.clientIdentifierDoesNotExist](./code/clientidentifierdoesnotexist.md)
  An error that indicates the client identifier doesn’t exist.
- [CNError.Code.communicationError](./code/communicationerror.md)
  An error that indicates a communication error occurred.
- [CNError.Code.containmentCycle](./code/containmentcycle.md)
  An error with the containment cycle.
- [CNError.Code.containmentScope](./code/containmentscope.md)
  An error with containment scope.
- [CNError.Code.dataAccessError](./code/dataaccesserror.md)
  An error with data access.
- [CNError.Code.featureDisabledByUser](./code/featuredisabledbyuser.md)
  An error that indicates the user disabled the feature.
- [CNError.Code.featureNotAvailable](./code/featurenotavailable.md)
  An error that indicates the feature isn’t available.
- [CNError.Code.insertedRecordAlreadyExists](./code/insertedrecordalreadyexists.md)
  An error that indicates the inserted record already exists.
- [CNError.Code.noAccessableWritableContainers](./code/noaccessablewritablecontainers.md)
  An error that indicates there are no accessible writable containers.
- [CNError.Code.parentContainerNotWritable](./code/parentcontainernotwritable.md)
  An error that indicates the parent container isn’t writable.
- [CNError.Code.parentRecordDoesNotExist](./code/parentrecorddoesnotexist.md)
  An error that indicates the parent record doesn’t exist.
- [CNError.Code.policyViolation](./code/policyviolation.md)
  An error that indicates a policy violation.
- [CNError.Code.predicateInvalid](./code/predicateinvalid.md)
  An error that indicates an invalid predicate.
- [CNError.Code.recordDoesNotExist](./code/recorddoesnotexist.md)
  An error that indicates a record doesn’t exist.
- [CNError.Code.recordIdentifierInvalid](./code/recordidentifierinvalid.md)
  An error that indicates a record identifier is invalid.
- [CNError.Code.recordNotWritable](./code/recordnotwritable.md)
  An error that indicates a record isn’t writable.
- [CNError.Code.unauthorizedKeys](./code/unauthorizedkeys.md)
  An error that indicates unauthorized keys usage.
- [CNError.Code.validationMultipleErrors](./code/validationmultipleerrors.md)
  An error that indicates the system encountered multiple validation errors.
- [CNError.Code.validationTypeMismatch](./code/validationtypemismatch.md)
  A validation error that indicates a type mismatch.
- [CNError.Code.validationConfigurationError](./code/validationconfigurationerror.md)
  An error with validation configuration.
- [CNError.Code.vCardMalformed](./code/vcardmalformed.md)
  An error that indicates a malformed vCard.
- [CNError.Code.vCardSummarizationError](./code/vcardsummarizationerror.md)
  An error that indicates a vCard summarization problem.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Error codes
- [struct CNError](../cnerror.md)
  Error information that may be returned when using the methods of the Contacts framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnerror/code)*