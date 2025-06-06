# Security Transforms

**Framework**: Security

Perform cryptographic functions like encoding, encryption, signing, and signature verification.

#### Overview

You use security transforms to assemble a chain of security-related operations that you apply to a stream of data in macOS.

## Topics

### Transforms
- [func SecTransformCreateReadTransformWithReadStream(CFReadStream) -> SecTransform](sectransformcreatereadtransformwithreadstream(_:).md)
  Creates a read transform from a read stream reference.
- [typealias SecTransform](sectransform.md)
  A Core Foundation type that represents a security transform.
- [func SecTransformGetTypeID() -> CFTypeID](sectransformgettypeid().md)
  Returns the unique identifier of the opaque type to which a security transform object belongs.
### Encoding
- [func SecEncodeTransformCreate(CFTypeRef, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](secencodetransformcreate(_:_:).md)
  Creates an encode transform object.
- [func SecDecodeTransformCreate(CFTypeRef, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](secdecodetransformcreate(_:_:).md)
  Creates a decode transform object.
### Encrypting
- [func SecEncryptTransformCreate(SecKey, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform](secencrypttransformcreate(_:_:).md)
  Creates an encryption transform object.
- [func SecDecryptTransformCreate(SecKey, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform](secdecrypttransformcreate(_:_:).md)
  Creates a decryption transform object.
- [func SecEncryptTransformGetTypeID() -> CFTypeID](secencrypttransformgettypeid().md)
  Returns the unique identifier of the opaque type to which an encryption transform belongs.
- [func SecDecryptTransformGetTypeID() -> CFTypeID](secdecrypttransformgettypeid().md)
  Returns the unique identifier of the opaque type to which a decryption transform belongs.
### Signing
- [func SecSignTransformCreate(SecKey, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](secsigntransformcreate(_:_:).md)
  Creates a signing transform object.
- [func SecVerifyTransformCreate(SecKey, CFData?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](secverifytransformcreate(_:_:_:).md)
  Creates a verify transform object.
- [func SecDigestTransformCreate(CFTypeRef?, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform](secdigesttransformcreate(_:_:_:).md)
  Creates a digest transform object.
- [func SecDigestTransformGetTypeID() -> CFTypeID](secdigesttransformgettypeid().md)
  Returns the unique identifier of the opaque type to which a digest transform belongs.
### Custom Transforms
- [func SecTransformCreate(CFString, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](sectransformcreate(_:_:).md)
  Creates a transform computation object.
- [func SecTransformRegister(CFString, SecTransformCreateFP, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](sectransformregister(_:_:_:).md)
  Registers a custom transform.
- [typealias SecTransformCreateFP](sectransformcreatefp.md)
  A pointer to a function that creates a new instance of a custom transform.
- [typealias SecTransformInstanceBlock](sectransforminstanceblock.md)
  A block that you return from a transform creation function.
- [typealias SecTransformImplementationRef](sectransformimplementationref.md)
  An opaque pointer to a block that implements an instance of a transform.
### Transform Groups
- [func SecTransformCreateGroupTransform() -> SecGroupTransform](sectransformcreategrouptransform().md)
  Creates an object that acts as a container for a set of connected transforms.
- [func SecTransformFindByName(SecGroupTransform, CFString) -> SecTransform?](sectransformfindbyname(_:_:).md)
  Finds a member of a transform group by its name.
- [typealias SecGroupTransform](secgrouptransform.md)
  A Core Foundation type that represents a container holding a group of transforms.
- [func SecGroupTransformGetTypeID() -> CFTypeID](secgrouptransformgettypeid().md)
  Returns the Core Foundation type ID for a transform group container.
### Transform Characteristics
- [func SecTransformSetAttribute(SecTransform, CFString, CFTypeRef, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](sectransformsetattribute(_:_:_:_:).md)
  Sets a static value for an attribute in a transform.
- [func SecTransformGetAttribute(SecTransform, CFString) -> CFTypeRef?](sectransformgetattribute(_:_:).md)
  Gets the current value of a transform attribute.
- [func SecTransformCustomSetAttribute(SecTransformImplementationRef, SecTransformStringOrAttribute, SecTransformMetaAttributeType, CFTypeRef?) -> CFTypeRef?](sectransformcustomsetattribute(_:_:_:_:).md)
  Sets an attribute value on a custom transform.
- [func SecTransformCustomGetAttribute(SecTransformImplementationRef, SecTransformStringOrAttribute, SecTransformMetaAttributeType) -> CFTypeRef?](sectransformcustomgetattribute(_:_:_:).md)
  Gets an attribute value from a custom transform.
- [func SecTransformPushbackAttribute(SecTransformImplementationRef, SecTransformStringOrAttribute, CFTypeRef) -> CFTypeRef?](sectransformpushbackattribute(_:_:_:).md)
  Pushes a single value back for a specific attribute.
- [Transform Attributes](transform-attributes.md)
  Specify the attributes of a transform.
- [typealias SecTransformAttribute](sectransformattribute.md)
  A direct reference to a security transform attribute.
- [typealias SecTransformStringOrAttribute](sectransformstringorattribute.md)
  A type that may be either a string or an attribute reference.
- [enum SecTransformMetaAttributeType](sectransformmetaattributetype.md)
  The keys that describe the metadata attributes of transform attributes.
### Actions
- [func SecTransformSetDataAction(SecTransformImplementationRef, CFString, SecTransformDataBlock) -> CFError?](sectransformsetdataaction(_:_:_:).md)
  Changes the way a custom transform processes data.
- [func SecTransformSetAttributeAction(SecTransformImplementationRef, CFString, SecTransformStringOrAttribute?, SecTransformAttributeActionBlock) -> CFError?](sectransformsetattributeaction(_:_:_:_:).md)
  Requests a callback when an attribute is set.
- [func SecTransformSetTransformAction(SecTransformImplementationRef, CFString, SecTransformActionBlock) -> CFError?](sectransformsettransformaction(_:_:_:).md)
  Changes the way that a transform deals with transform lifecycle behaviors.
- [typealias SecTransformActionBlock](sectransformactionblock.md)
  A block that overrides the default behavior of a custom transform.
- [typealias SecTransformAttributeActionBlock](sectransformattributeactionblock.md)
  A block used to override the default attribute handling for when an attribute is set.
- [typealias SecTransformDataBlock](sectransformdatablock.md)
  A block used to override the default data handling for a transform.
- [Actions](actions.md)
  Use actions to trigger particular behaviors.
### Piping
- [func SecTransformConnectTransforms(SecTransform, CFString, SecTransform, CFString, SecGroupTransform, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecGroupTransform?](sectransformconnecttransforms(_:_:_:_:_:_:).md)
  Chains transforms together.
### Execution
- [func SecTransformExecute(SecTransform, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFTypeRef](sectransformexecute(_:_:).md)
  Executes a transform or transform group synchronously.
- [func SecTransformExecuteAsync(SecTransform, dispatch_queue_t, SecMessageBlock)](sectransformexecuteasync(_:_:_:).md)
  Executes transform or transform group asynchronously.
- [func SecTransformNoData() -> CFTypeRef](sectransformnodata().md)
  Returns an object from inside a ProcessData override that says that although no data is being returned the transform is still active and awaiting data.
- [typealias SecMessageBlock](secmessageblock.md)
  A block that delivers messages during asynchronous operations.
### Import and Export
- [func SecTransformCopyExternalRepresentation(SecTransform) -> CFDictionary](sectransformcopyexternalrepresentation(_:).md)
  Creates a dictionary that contains enough information to be able to recreate a transform.
- [func SecTransformCreateFromExternalRepresentation(CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](sectransformcreatefromexternalrepresentation(_:_:).md)
  Creates a transform instance from a dictionary of parameters.
### Reporting Errors
- [let kSecTransformErrorDomain: CFString](ksectransformerrordomain.md)
  The domain of any error object created by a transform on failure.
- [Security Transform Error Codes](security-transform-error-codes.md)
  Recognize the error codes used in error objects created by a transform on failure.
- [let kSecTransformPreviousErrorKey: CFString](ksectransformpreviouserrorkey.md)
  The key in an error’s `userInfo` dictionary whose value specifies the previous error when multiple errors occur during transform evaluation.
- [let kSecTransformAbortOriginatorKey: CFString](ksectransformabortoriginatorkey.md)
  The key in an error’s `userInfo` dictionary whose value indicates the transform that caused the chain to abort.

## See Also

- [Security Transforms Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecTransformPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010801)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/security-transforms)*