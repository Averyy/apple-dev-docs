# CFErrorCopyUserInfo(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the user info dictionary for a given CFError.

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
func CFErrorCopyUserInfo(_ err: CFError!) -> CFDictionary!
```

```c
extern CFDictionaryRefCFErrorCopyUserInfo(CFErrorRef err);
```

#### Return Value

A dictionary containing the same keys and values as in the userInfo dictionary `err` was created with. Returns an empty dictionary if `NULL` was supplied to the create function. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `err`: The error to examine. If this is not a valid CFError, the behavior is undefined.

## See Also

### Getting Information About an Error
- [func CFErrorGetDomain(CFError!) -> CFErrorDomain!](./cferrorgetdomain%28_%29.md)
  Returns the error domain for a given CFError.
- [func CFErrorGetCode(CFError!) -> CFIndex](./cferrorgetcode%28_%29.md)
  Returns the error code for a given CFError.
- [func CFErrorCopyDescription(CFError!) -> CFString!](./cferrorcopydescription%28_%29.md)
  Returns a human-presentable description for a given error.
- [func CFErrorCopyFailureReason(CFError!) -> CFString!](./cferrorcopyfailurereason%28_%29.md)
  Returns a human-presentable failure reason for a given error.
- [func CFErrorCopyRecoverySuggestion(CFError!) -> CFString!](./cferrorcopyrecoverysuggestion%28_%29.md)
  Returns a human presentable recovery suggestion for a given error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cferrorcopyuserinfo(_:))*