# Security Transform Error Codes

**Framework**: Security

Recognize the error codes used in error objects created by a transform on failure.

## Topics

### Constants
- [var kSecTransformErrorAttributeNotFound: CFIndex](ksectransformerrorattributenotfound.md)
  The attribute was not found.
- [var kSecTransformErrorInvalidOperation: CFIndex](ksectransformerrorinvalidoperation.md)
  An invalid operation was attempted.
- [var kSecTransformErrorNotInitializedCorrectly: CFIndex](ksectransformerrornotinitializedcorrectly.md)
  A required initialization is missing: It is most likely a missing required attribute.
- [var kSecTransformErrorMoreThanOneOutput: CFIndex](ksectransformerrormorethanoneoutput.md)
  A transform has an internal routing error that has caused multiple outputs instead of a single discrete output.
- [var kSecTransformErrorInvalidInputDictionary: CFIndex](ksectransformerrorinvalidinputdictionary.md)
  A dictionary used to import a transform has invalid data.
- [var kSecTransformErrorInvalidAlgorithm: CFIndex](ksectransformerrorinvalidalgorithm.md)
  A transform that needs an algorithm as an attribute received an invalid algorithm.
- [var kSecTransformErrorInvalidLength: CFIndex](ksectransformerrorinvalidlength.md)
  A transform that needs a length such as a digest transform has been given an invalid length.
- [var kSecTransformErrorInvalidType: CFIndex](ksectransformerrorinvalidtype.md)
  An invalid type has been set on an attribute.
- [var kSecTransformErrorInvalidInput: CFIndex](ksectransformerrorinvalidinput.md)
  The input set on a transform is invalid.
- [var kSecTransformErrorNameAlreadyRegistered: CFIndex](ksectransformerrornamealreadyregistered.md)
  A custom transform of a particular name has already been registered.
- [var kSecTransformErrorUnsupportedAttribute: CFIndex](ksectransformerrorunsupportedattribute.md)
  An illegal action such as setting a read-only attribute has occurred.
- [var kSecTransformOperationNotSupportedOnGroup: CFIndex](ksectransformoperationnotsupportedongroup.md)
  An illegal action on a group transform has occurred.
- [var kSecTransformErrorMissingParameter: CFIndex](ksectransformerrormissingparameter.md)
  A transform is missing a required attribute.
- [var kSecTransformErrorInvalidConnection: CFIndex](ksectransformerrorinvalidconnection.md)
  A connection between transforms in different groups was attempted.
- [var kSecTransformTransformIsExecuting: CFIndex](ksectransformtransformisexecuting.md)
  An illegal operation was called on a Transform while it was executing.
- [var kSecTransformInvalidOverride: CFIndex](ksectransforminvalidoverride.md)
  An illegal override was given to a custom transform.
- [var kSecTransformTransformIsNotRegistered: CFIndex](ksectransformtransformisnotregistered.md)
  A custom transform was asked to be created but the transform has not been registered.
- [var kSecTransformErrorAbortInProgress: CFIndex](ksectransformerrorabortinprogress.md)
  The abort attribute has been set and the transform is in the process of shutting down.
- [var kSecTransformErrorAborted: CFIndex](ksectransformerroraborted.md)
  The transform was aborted.
- [var kSecTransformInvalidArgument: CFIndex](ksectransforminvalidargument.md)
  An invalid argument was given to a Transform API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/security-transform-error-codes)*