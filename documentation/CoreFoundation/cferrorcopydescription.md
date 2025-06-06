# CFErrorCopyDescription(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a human-presentable description for a given error.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFErrorCopyDescription(_ err: CFError!) -> CFString!
```

#### Return Value

A localized, human-presentable description of `err`. This function never returns `NULL`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This is a complete sentence or two which says what failed and why it failed. The structure of the description depends on the details provided in the user info dictionary. The rules for computing the return value are as follows:

1. If the value in the user info dictionary for [`kCFErrorLocalizedDescriptionKey`](kcferrorlocalizeddescriptionkey.md) is not `NULL`, it returns that value as-is.
2. If the value in the user info dictionary for [`kCFErrorLocalizedFailureReasonKey`](kcferrorlocalizedfailurereasonkey.md) is not `NULL`, there will be an error generated from that.

The description is something like: “Operation could not be completed. “ + `kCFErrorLocalizedFailureReasonKey` 3. Generate a user-presentable string from [`kCFErrorDescriptionKey`](kcferrordescriptionkey.md), the domain, and code.

The description is something like: “Operation could not be completed. Error domain/code occurred. “ or “Operation could not be completed. “ + `kCFErrorDescriptionKey` + “ (Error domain/code)”

Toll-free bridged instances of [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) might provide additional behaviors for manufacturing a description string.

You should not depend on the exact contents or format of the returned string, as it might change in different releases of the operating system.

When you create a [`CFError`](cferror.md), you should try to make sure the return value is human-presentable and localized by providing a value for [`kCFErrorLocalizedDescriptionKey`](kcferrorlocalizeddescriptionkey.md) in the user info dictionary.

## Parameters

- `err`: The   to examine. If this is not a valid  , the behavior is undefined.

## See Also

- [func CFErrorGetDomain(CFError!) -> CFErrorDomain!](cferrorgetdomain(_:).md)
  Returns the error domain for a given CFError.
- [func CFErrorGetCode(CFError!) -> CFIndex](cferrorgetcode(_:).md)
  Returns the error code for a given CFError.
- [func CFErrorCopyUserInfo(CFError!) -> CFDictionary!](cferrorcopyuserinfo(_:).md)
  Returns the user info dictionary for a given CFError.
- [func CFErrorCopyFailureReason(CFError!) -> CFString!](cferrorcopyfailurereason(_:).md)
  Returns a human-presentable failure reason for a given error.
- [func CFErrorCopyRecoverySuggestion(CFError!) -> CFString!](cferrorcopyrecoverysuggestion(_:).md)
  Returns a human presentable recovery suggestion for a given error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cferrorcopydescription(_:))*