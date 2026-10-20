# NSError

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

Information about an error condition including a domain, a domain-specific error code, and application-specific information.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSError
```

```objc
@interface NSError : NSObject
```

#### Overview

Objective-C methods can signal an error condition by returning an [`NSError`](./nserror.md) object by reference, which provides additional information about the kind of error and any underlying cause, if one can be determined. An [`NSError`](./nserror.md) object may also provide localized error descriptions suitable for display to the user in its user info dictionary. See [Error Handling Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorHandling/ErrorHandling.html#//apple_ref/doc/uid/TP40001806) for more information.

Methods in Foundation and other Cocoa frameworks most often produce errors in the Cocoa error domain ([`NSCocoaErrorDomain`](./nscocoaerrordomain.md)); error codes for the Cocoa Error Domain are documented in the [Foundation Constants](./foundation-constants.md). There are also predefined domains corresponding to Mach ([`NSMachErrorDomain`](./nsmacherrordomain.md)), POSIX ([`NSPOSIXErrorDomain`](./nsposixerrordomain.md)), and Carbon ([`NSOSStatusErrorDomain`](./nsosstatuserrordomain.md)) errors.

[`NSError`](./nserror.md) is “toll-free bridged” with its Core Foundation counterpart, [`CFError`](../CoreFoundation/cferror.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

##### Subclassing Notes

Applications may choose to create subclasses of `NSError`, for example, to provide better localized error strings by overriding [`localizedDescription`](./nserror/localizeddescription.md).

## Topics

### Creating Error Objects
- [init(domain: String, code: Int, userInfo: [String : Any]?)](./nserror/init%28domain,code,userinfo%29.md)
  Returns an `NSError` object initialized for a given domain and code with a given `userInfo` dictionary.
### Getting Error Properties
- [var code: Int](./nserror/code.md)
  The error code.
- [var domain: String](./nserror/domain.md)
  A string containing the error domain.
- [var userInfo: [String : Any]](./nserror/userinfo.md)
  The user info dictionary.
### Getting a Localized Error Description
- [var localizedDescription: String](./nserror/localizeddescription.md)
  A string containing the localized description of the error.
- [var localizedRecoveryOptions: [String]?](./nserror/localizedrecoveryoptions.md)
  An array containing the localized titles of buttons appropriate for displaying in an alert panel.
- [var localizedRecoverySuggestion: String?](./nserror/localizedrecoverysuggestion.md)
  A string containing the localized recovery suggestion for the error.
- [var localizedFailureReason: String?](./nserror/localizedfailurereason.md)
  A string containing the localized explanation of the reason for the error.
### Providing Error User Info
- [class func setUserInfoValueProvider(forDomain: String, provider: ((any Error, String) -> Any?)?)](./nserror/setuserinfovalueprovider%28fordomain,provider%29.md)
  Specifies a block to call when the corresponding property is not present in the user info dictionary.
- [class func userInfoValueProvider(forDomain: String) -> ((any Error, String) -> Any?)?](./nserror/userinfovalueprovider%28fordomain%29.md)
  Returns any user info provider specified for a given error domain.
- [struct ErrorUserInfoKey](./erroruserinfokey.md)
  These keys may exist in the user info dictionary.
- [typealias UserInfoKey](./nserror/userinfokey.md)
  These keys may exist in the user info dictionary.
### Getting the Error Recovery Attempter
- [var recoveryAttempter: Any?](./nserror/recoveryattempter.md)
  The object in the user info dictionary corresponding to the [`NSRecoveryAttempterErrorKey`](./nsrecoveryattemptererrorkey.md) key.
- [NSErrorRecoveryAttempting](./nserrorrecoveryattempting.md)
  A set of methods that provide options to recover from an error.
### Displaying a Help Anchor
- [var helpAnchor: String?](./nserror/helpanchor.md)
  A string to display in response to an alert panel help anchor button being pressed.
### Supporting Types
- [typealias ErrorPointer](./errorpointer.md)
- [typealias NSErrorPointer](./nserrorpointer.md)
- [typealias NSErrorDomain](./nserrordomain.md)
### Error Domains
- [let NSCocoaErrorDomain: String](./nscocoaerrordomain.md)
  Cocoa errors
- [let NSPOSIXErrorDomain: String](./nsposixerrordomain.md)
  POSIX/BSD errors
- [let NSOSStatusErrorDomain: String](./nsosstatuserrordomain.md)
  Mac OS 9/Carbon errors
- [let NSMachErrorDomain: String](./nsmacherrordomain.md)
  Mach errors
- [let NSURLErrorDomain: String](./nsurlerrordomain.md)
  URL loading system errors
- [let NSStreamSOCKSErrorDomain: String](./nsstreamsockserrordomain.md)
  The error domain used by `NSError` when reporting SOCKS errors.
- [let NSStreamSocketSSLErrorDomain: String](./nsstreamsocketsslerrordomain.md)
  The error domain used by `NSError` when reporting SSL errors.
### Error Codes
- [struct CocoaError](./cocoaerror.md)
  Describes errors within the Cocoa error domain.
- [struct MachError](./macherror.md)
  Describes an error in the Mach error domain.
- [struct POSIXError](./posixerror.md)
  Describes an error in the POSIX error domain.
- [NSError Codes](./api-1448136-nserror-codes.md)
  Error codes in the Cocoa error domain.
### Initializers
- [convenience init()](./nserror/init%28%29.md)
- [init?(coder: NSCoder)](./nserror/init%28coder%29.md)
### Instance Properties
- [var underlyingErrors: [any Error]](./nserror/underlyingerrors.md)
### Type Methods
- [class func fileProviderErrorForCollision(with: NSFileProviderItem) -> Self](./nserror/fileprovidererrorforcollision%28with%29.md)
  Returns a properly formatted error object with a `NSFileProviderItemCollisionError` error code.
- [class func fileProviderErrorForNonExistentItem(withIdentifier: NSFileProviderItemIdentifier) -> Self](./nserror/fileprovidererrorfornonexistentitem%28withidentifier%29.md)
- [class func fileProviderErrorForRejectedDeletion(of: NSFileProviderItem) -> Self](./nserror/fileprovidererrorforrejecteddeletion%28of%29.md)
- [class func new() -> Self](./nserror/new%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### User-Relevant Errors
- [protocol Error](../Swift/error.md)
  A type representing an error value that can be thrown.
- [protocol LocalizedError](./localizederror.md)
  A specialized error that provides localized messages describing the error and why it occurred.
- [protocol RecoverableError](./recoverableerror.md)
  A specialized error that may be recoverable by presenting several potential recovery options to the user.
- [protocol CustomNSError](./customnserror.md)
  A specialized error that provides a domain, error code, and user-info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror)*