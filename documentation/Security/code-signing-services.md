# Code Signing Services

**Framework**: Security

Examine and validate signed code running on the system.

#### Overview

Code signing is a macOS security technology that you use to certify that an app was created by you. Once an app is signed, the system can detect any change to the app—whether the change is introduced accidentally or by malicious code. You can control how your signed code loads signed plug-ins and other signed code without invalidating the signatures of the host code or of the guest (dynamically loaded) code.

You work with code objects that represent uniquely identified elements of running code in the system. In addition to UNIX processes, these elements can include scripts, applets, widgets, and so forth. You also work with  code objects that represent code in the file system. Static code includes applications, tools, frameworks, plug-ins, scripts, and so on. Generally, a code object has a specific static code object from which it originates and that holds its static signing data. The reverse, however, is not true—given a static code object, it is not possible to find, enumerate, or control any code object that originated from it.

## Topics

### Code Objects
- [class SecCode](seccode.md)
  A code object representing signed code running on the system.
- [func SecCodeCopySelf(SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyself(_:_:).md)
  Retrieves the code object for the code making the call.
- [struct SecCSFlags](seccsflags.md)
  Values that can be used in the `flags` parameter to most code signing functions.
- [func SecCodeGetTypeID() -> CFTypeID](seccodegettypeid().md)
  Returns the unique identifier of the opaque type to which a code object belongs.
### Static Code
- [class SecStaticCode](secstaticcode.md)
  A static code object representing signed code on disk.
- [func SecStaticCodeCreateWithPath(CFURL, SecCSFlags, UnsafeMutablePointer<SecStaticCode?>) -> OSStatus](secstaticcodecreatewithpath(_:_:_:).md)
  Creates a static code object representing the code at a specified file system path.
- [func SecStaticCodeCreateWithPathAndAttributes(CFURL, SecCSFlags, CFDictionary, UnsafeMutablePointer<SecStaticCode?>) -> OSStatus](secstaticcodecreatewithpathandattributes(_:_:_:_:).md)
  Creates a static code object representing the code at a specified file system path using an attributes dictionary.
- [Code Attributes](code-attributes.md)
  Specify these keys from the attribute dictionary when you create a static code instance.
- [func SecStaticCodeGetTypeID() -> CFTypeID](secstaticcodegettypeid().md)
  Returns the unique identifier of the opaque type to which a static code object belongs.
### Working with Code Objects
- [func SecCodeCopyPath(SecStaticCode, SecCSFlags, UnsafeMutablePointer<CFURL?>) -> OSStatus](seccodecopypath(_:_:_:).md)
  Retrieves the location on disk of signed code, given a code or static code object.
- [func SecCodeCopyStaticCode(SecCode, SecCSFlags, UnsafeMutablePointer<SecStaticCode?>) -> OSStatus](seccodecopystaticcode(_:_:_:).md)
  Returns a static code object representing the on-disk version of the given running code.
- [Code Signing Architecture Flags](code-signing-architecture-flags.md)
  Use these supplemental flags to get static code.
### Code Signatures
- [func SecCodeCopySigningInformation(SecStaticCode, SecCSFlags, UnsafeMutablePointer<CFDictionary?>) -> OSStatus](seccodecopysigninginformation(_:_:_:).md)
  Retrieves various pieces of information from a code signature.
- [Code Signing Information Flags](code-signing-information-flags.md)
  Use these supplemental flags to retrieve signing information.
- [Signing Information Dictionary Keys](signing-information-dictionary-keys.md)
  Use these keys from the information dictionary when you retrieve information from a code signature.
- [struct SecCodeSignatureFlags](seccodesignatureflags.md)
  Specify option flags that can be embedded in a code signature during signing and that govern the use of the signature.
- [enum SecCSDigestAlgorithm](seccsdigestalgorithm.md)
  The list of digest algorithms available for code signatures.
### Code Requirements
- [Applying Code Requirements](applying-code-requirements.md)
  Manage the code requirements that apply to your signed code.
- [func SecCodeCopyDesignatedRequirement(SecStaticCode, SecCSFlags, UnsafeMutablePointer<SecRequirement?>) -> OSStatus](seccodecopydesignatedrequirement(_:_:_:).md)
  Retrieves the designated code requirement of signed code.
- [class SecRequirement](secrequirement.md)
  A code requirement object.
- [func SecRequirementGetTypeID() -> CFTypeID](secrequirementgettypeid().md)
  Returns the unique identifier of the opaque type to which a code requirement object belongs.
- [enum SecRequirementType](secrequirementtype.md)
  An enumeration indicating different types of internal requirements for code.
### Code Requirements as Data
- [func SecRequirementCopyData(SecRequirement, SecCSFlags, UnsafeMutablePointer<CFData?>) -> OSStatus](secrequirementcopydata(_:_:_:).md)
  Extracts a binary form of a code requirement from a code requirement object.
- [func SecRequirementCreateWithData(CFData, SecCSFlags, UnsafeMutablePointer<SecRequirement?>) -> OSStatus](secrequirementcreatewithdata(_:_:_:).md)
  Creates a code requirement object from the binary form of a code requirement.
### Code Requirements as Text
- [func SecRequirementCopyString(SecRequirement, SecCSFlags, UnsafeMutablePointer<CFString?>) -> OSStatus](secrequirementcopystring(_:_:_:).md)
  Converts a code requirement object into text form.
- [func SecRequirementCreateWithString(CFString, SecCSFlags, UnsafeMutablePointer<SecRequirement?>) -> OSStatus](secrequirementcreatewithstring(_:_:_:).md)
  Creates a code requirement object by compiling a valid text representation of a code requirement.
- [func SecRequirementCreateWithStringAndErrors(CFString, SecCSFlags, UnsafeMutablePointer<Unmanaged<CFError>?>?, UnsafeMutablePointer<SecRequirement?>) -> OSStatus](secrequirementcreatewithstringanderrors(_:_:_:_:).md)
  Creates a code requirement object by compiling a valid text representation of a code requirement and returns detailed error information in the case of failure.
### Guest Code
- [Hosting Guest Code](hosting-guest-code.md)
  Securely launch and manage plug-ins and other executable entities, known as guest code, from within your app acting as a host.
- [func SecCodeCopyGuestWithAttributes(SecCode?, CFDictionary?, SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyguestwithattributes(_:_:_:_:).md)
  Asks a code host to identify one of its guests given the type and value of specific attributes of the guest code.
- [Null Guest Handle](null-guest-handle.md)
  Use this special value to stand in for a null guest object.
- [struct SecCodeStatus](seccodestatus.md)
  Operational flags attached by code signing services to running code.
- [Guest Creation Flags](guest-creation-flags.md)
  Use these supplemental flags to create a guest object.
- [Guest Attribute Dictionary Keys](guest-attribute-dictionary-keys.md)
  Specify attributes of guest code.
- [typealias SecGuestRef](secguestref.md)
  A reference to a guest object, which identifies a particular block of guest code in the context of its code signing host.
### Guest Management
- [func SecCodeCopyHost(SecCode, SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyhost(_:_:_:).md)
  Retrieves the code object for the host of specified guest code.
- [func SecCodeMapMemory(SecStaticCode, SecCSFlags) -> OSStatus](seccodemapmemory(_:_:).md)
  Asks the kernel to accept the signing information currently attached to a code object and uses it to validate memory page-ins.
### Tasks
- [func SecTaskCreateFromSelf(CFAllocator?) -> SecTask?](sectaskcreatefromself(_:).md)
  Creates a task object for the current task.
- [func SecTaskCreateWithAuditToken(CFAllocator?, audit_token_t) -> SecTask?](sectaskcreatewithaudittoken(_:_:).md)
  Creates a task object for the task that sent the Mach message represented by the audit token.
- [class SecTask](sectask.md)
  The Core Foundation type representing a task.
- [func SecTaskGetTypeID() -> CFTypeID](sectaskgettypeid().md)
  Returns the unique identifier of the opaque type to which a task object belongs.
- [func SecTaskCopySigningIdentifier(SecTask, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?](sectaskcopysigningidentifier(_:_:).md)
  Returns the value of the code signing identifier.
- [func SecTaskCopyValueForEntitlement(SecTask, CFString, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFTypeRef?](sectaskcopyvalueforentitlement(_:_:_:).md)
  Returns the value of a single entitlement for the represented task.
- [func SecTaskCopyValuesForEntitlements(SecTask, CFArray, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary?](sectaskcopyvaluesforentitlements(_:_:_:).md)
  Returns the values of multiple entitlements for the represented task.
### Code Signature Validity
- [func SecCodeCheckValidity(SecCode, SecCSFlags, SecRequirement?) -> OSStatus](seccodecheckvalidity(_:_:_:).md)
  Performs dynamic validation of signed code.
- [func SecCodeCheckValidityWithErrors(SecCode, SecCSFlags, SecRequirement?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OSStatus](seccodecheckvaliditywitherrors(_:_:_:_:).md)
  Performs dynamic validation of signed code and returns detailed error information in the case of failure.
- [func SecStaticCodeCheckValidity(SecStaticCode, SecCSFlags, SecRequirement?) -> OSStatus](secstaticcodecheckvalidity(_:_:_:).md)
  Validates a static code object.
- [func SecStaticCodeCheckValidityWithErrors(SecStaticCode, SecCSFlags, SecRequirement?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OSStatus](secstaticcodecheckvaliditywitherrors(_:_:_:_:).md)
  Performs static validation of static signed code and returns detailed error information in the case of failure.
- [Static Code Validation Flags](static-code-validation-flags.md)
  Use these supplemental flags to test the validity of a static code signature.
### Result Codes
- [Code Signing Services Result Codes](code-signing-services-result-codes.md)
  Recognize result codes specific to the code signing services API.
- [User Info Dictionary Error Keys](user-info-dictionary-error-keys.md)
  Recognize the keys of the user info dictionary provided by functions that return error objects.

## See Also

- [Code Signing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005929)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/code-signing-services)*