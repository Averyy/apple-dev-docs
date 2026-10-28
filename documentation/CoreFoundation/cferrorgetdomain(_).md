# CFErrorGetDomain(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the error domain for a given CFError.

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
func CFErrorGetDomain(_ err: CFError!) -> CFErrorDomain!
```

```c
extern CFErrorDomainCFErrorGetDomain(CFErrorRef err);
```

## Return Value

The error domain for `err`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `err`: The error to examine. If this is not a valid CFError, the behavior is undefined.

## See Also

### Getting Information About an Error
- [func CFErrorGetCode(CFError!) -> CFIndex](./cferrorgetcode%28_%29.md)
  Returns the error code for a given CFError.
- [func CFErrorCopyUserInfo(CFError!) -> CFDictionary!](./cferrorcopyuserinfo%28_%29.md)
  Returns the user info dictionary for a given CFError.
- [func CFErrorCopyDescription(CFError!) -> CFString!](./cferrorcopydescription%28_%29.md)
  Returns a human-presentable description for a given error.
- [func CFErrorCopyFailureReason(CFError!) -> CFString!](./cferrorcopyfailurereason%28_%29.md)
  Returns a human-presentable failure reason for a given error.
- [func CFErrorCopyRecoverySuggestion(CFError!) -> CFString!](./cferrorcopyrecoverysuggestion%28_%29.md)
  Returns a human presentable recovery suggestion for a given error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cferrorgetdomain(_:))*