# CXCallDirectoryExtensionContext

**Framework**: CallKit  
**Kind**: class

A programmatic interface for adding identification and blocking entries to a Call Directory app extension.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
class CXCallDirectoryExtensionContext
```

#### Overview

The system doesn’t initialize [`CXCallDirectoryExtensionContext`](cxcalldirectoryextensioncontext.md) objects directly, but instead passes them as arguments to the [`CXCallDirectoryProvider`](cxcalldirectoryprovider.md) instance method [`beginRequest(with:)`](cxcalldirectoryprovider/beginrequest(with:).md).

## Topics

### Setting the Delegate
- [var delegate: (any CXCallDirectoryExtensionContextDelegate)?](cxcalldirectoryextensioncontext/delegate.md)
  Sets a delegate that can handle request failures for the Call Directory extension context object.
### Adding Entries
- [func addIdentificationEntry(withNextSequentialPhoneNumber: CXCallDirectoryPhoneNumber, label: String)](cxcalldirectoryextensioncontext/addidentificationentry(withnextsequentialphonenumber:label:).md)
  Adds an identification entry with the specified phone number and label.
- [func addBlockingEntry(withNextSequentialPhoneNumber: CXCallDirectoryPhoneNumber)](cxcalldirectoryextensioncontext/addblockingentry(withnextsequentialphonenumber:).md)
  Adds a blocking entry with the specified phone number.
### Removing Entries
- [func removeAllBlockingEntries()](cxcalldirectoryextensioncontext/removeallblockingentries.md)
  Removes all stored blocking entries.
- [func removeAllIdentificationEntries()](cxcalldirectoryextensioncontext/removeallidentificationentries.md)
  Removes all stored identification entries.
- [func removeBlockingEntry(withPhoneNumber: CXCallDirectoryPhoneNumber)](cxcalldirectoryextensioncontext/removeblockingentry(withphonenumber:).md)
  Removes a blocking entry that contains the specified phone number.
- [func removeIdentificationEntry(withPhoneNumber: CXCallDirectoryPhoneNumber)](cxcalldirectoryextensioncontext/removeidentificationentry(withphonenumber:).md)
  Removes an identification entry that contains the specified phone number.
### Completing Requests
- [var isIncremental: Bool](cxcalldirectoryextensioncontext/isincremental.md)
  A Boolean value that indicates whether the request provides data incrementally.
- [func completeRequest(completionHandler: ((Bool) -> Void)?)](cxcalldirectoryextensioncontext/completerequest(completionhandler:).md)
  Completes the request to the extension context.
### Types
- [typealias CXCallDirectoryPhoneNumber](cxcalldirectoryphonenumber.md)
  A value that represents a phone number consisting of a country calling code followed by a sequence of digits.
- [let CXCallDirectoryPhoneNumberMax: CXCallDirectoryPhoneNumber](cxcalldirectoryphonenumbermax.md)
  The maximum allowable value for a phone number.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/NSExtensionContext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Identifying and blocking calls](identifying-and-blocking-calls.md)
  Create a Call Directory app extension to identify and block incoming callers by their phone number.
- [class CXCallDirectoryProvider](cxcalldirectoryprovider.md)
  The principal object for a Call Directory app extension for a host app.
- [protocol CXCallDirectoryExtensionContextDelegate](cxcalldirectoryextensioncontextdelegate.md)
  A collection of methods a Call Directory extension context object calls when a request fails.
- [class CXCallDirectoryManager](cxcalldirectorymanager.md)
  The programmatic interface to an object that manages a Call Directory app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext)*