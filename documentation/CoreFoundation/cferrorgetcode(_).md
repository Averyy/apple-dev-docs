# CFErrorGetCode(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the error code for a given CFError.

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
func CFErrorGetCode(_ err: CFError!) -> CFIndex
```

```c
extern CFIndex CFErrorGetCode(CFErrorRef err);
```

#### Return Value

The error code of `err`.

#### Discussion

Note that this function returns the error code for the specified CFError, not an error return for the current call.

## Parameters

- `err`: The error to examine. If this is not a valid CFError, the behavior is undefined.

## See Also

### Getting Information About an Error
- [func CFErrorGetDomain(CFError!) -> CFErrorDomain!](./cferrorgetdomain%28_%29.md)
  Returns the error domain for a given CFError.
- [func CFErrorCopyUserInfo(CFError!) -> CFDictionary!](./cferrorcopyuserinfo%28_%29.md)
  Returns the user info dictionary for a given CFError.
- [func CFErrorCopyDescription(CFError!) -> CFString!](./cferrorcopydescription%28_%29.md)
  Returns a human-presentable description for a given error.
- [func CFErrorCopyFailureReason(CFError!) -> CFString!](./cferrorcopyfailurereason%28_%29.md)
  Returns a human-presentable failure reason for a given error.
- [func CFErrorCopyRecoverySuggestion(CFError!) -> CFString!](./cferrorcopyrecoverysuggestion%28_%29.md)
  Returns a human presentable recovery suggestion for a given error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cferrorgetcode(_:))*