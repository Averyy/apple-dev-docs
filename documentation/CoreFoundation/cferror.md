# CFError

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFError
```

#### Overview

A CFError object encapsulates more rich and extensible error information than is possible using only an error code or error string. The core attributes of a CFError object are an error domain (represented by a string), a domain-specific error code, and a “user info” dictionary containing application-specific information. Errors are required to have a domain and an error code within that domain. Several well-known domains are defined corresponding to Mach, POSIX, and OSStatus errors.

The optional “user info” dictionary may provide additional information that might be useful for the interpretation and reporting of the error, including a human-readable description for the error. The “user info” dictionary sometimes includes another CFError object that represents an error in a subsystem underlying the error represented by the containing CFError object. This underlying error object may provide more specific information about the cause of the error.

In general, a method should signal an error condition by returning, for example, `false` or `NULL` rather than by the simple presence of an error object. The method can then optionally return an CFError object by reference, in order to further describe the error.

CFError is toll-free bridged to [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) in the Foundation framework—for more details on toll-free bridging, see [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677). `NSError` has some additional guidelines that make it easy to report errors automatically to users and attempt to recover from them. See [`Error Handling Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorHandling/ErrorHandling.html#//apple_ref/doc/uid/TP40001806) for more information on `NSError` programming guidelines.

## Topics

### Creating a CFError
- [func CFErrorCreate(CFAllocator!, CFErrorDomain!, CFIndex, CFDictionary!) -> CFError!](cferrorcreate(_:_:_:_:).md)
  Creates a new CFError object.
- [func CFErrorCreateWithUserInfoKeysAndValues(CFAllocator!, CFErrorDomain!, CFIndex, UnsafePointer<UnsafeRawPointer?>!, UnsafePointer<UnsafeRawPointer?>!, CFIndex) -> CFError!](cferrorcreatewithuserinfokeysandvalues(_:_:_:_:_:_:).md)
  Creates a new CFError object using given keys and values to create the user info dictionary.
### Getting Information About an Error
- [func CFErrorGetDomain(CFError!) -> CFErrorDomain!](cferrorgetdomain(_:).md)
  Returns the error domain for a given CFError.
- [func CFErrorGetCode(CFError!) -> CFIndex](cferrorgetcode(_:).md)
  Returns the error code for a given CFError.
- [func CFErrorCopyUserInfo(CFError!) -> CFDictionary!](cferrorcopyuserinfo(_:).md)
  Returns the user info dictionary for a given CFError.
- [func CFErrorCopyDescription(CFError!) -> CFString!](cferrorcopydescription(_:).md)
  Returns a human-presentable description for a given error.
- [func CFErrorCopyFailureReason(CFError!) -> CFString!](cferrorcopyfailurereason(_:).md)
  Returns a human-presentable failure reason for a given error.
- [func CFErrorCopyRecoverySuggestion(CFError!) -> CFString!](cferrorcopyrecoverysuggestion(_:).md)
  Returns a human presentable recovery suggestion for a given error.
### Getting the CFError Type ID
- [func CFErrorGetTypeID() -> CFTypeID](cferrorgettypeid().md)
  Returns the type identifier for the CFError opaque type.
### Constants
- [Error domains](error-domains.md)
  These constants define domains for CFError objects.
- [Keys for the user info dictionary](keys-for-the-user-info-dictionary.md)
  Keys in the `userInfo` dictionary.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Error Handling Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorHandling/ErrorHandling.html#//apple_ref/doc/uid/TP40001806)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cferror)*