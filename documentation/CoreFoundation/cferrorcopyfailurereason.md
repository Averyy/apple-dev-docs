# CFErrorCopyFailureReason(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a human-presentable failure reason for a given error.

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
func CFErrorCopyFailureReason(_ err: CFError!) -> CFString!
```

#### Return Value

A localized, human-presentable failure reason for `err`, or `NULL` if no user-presentable string is available. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The failure reason is a complete sentence which describes why the operation failed. In many cases this will be just the “because” part of the description (but as a complete sentence, which makes localization easier). For example, an error description “Could not save file ‘Letter’ in folder ‘Documents’ because the volume ‘MyDisk’ doesn’t have enough space.” might have a corresponding failure reason, “The volume ‘MyDisk’ doesn’t have enough space.”

By default, this function looks for a value for the [`kCFErrorLocalizedFailureReasonKey`](kcferrorlocalizedfailurereasonkey.md) key in the user info dictionary. Toll-free bridged instances of `NSError` might provide additional behaviors for manufacturing this value.

When you create a CFError, you should try to make sure the return value is human-presentable and localized by providing a value for [`kCFErrorLocalizedFailureReasonKey`](kcferrorlocalizedfailurereasonkey.md) in the user info dictionary.

## Parameters

- `err`: The CFError to examine. If this is not a valid CFError, the behavior is undefined.

## See Also

- [func CFErrorGetDomain(CFError!) -> CFErrorDomain!](cferrorgetdomain(_:).md)
  Returns the error domain for a given CFError.
- [func CFErrorGetCode(CFError!) -> CFIndex](cferrorgetcode(_:).md)
  Returns the error code for a given CFError.
- [func CFErrorCopyUserInfo(CFError!) -> CFDictionary!](cferrorcopyuserinfo(_:).md)
  Returns the user info dictionary for a given CFError.
- [func CFErrorCopyDescription(CFError!) -> CFString!](cferrorcopydescription(_:).md)
  Returns a human-presentable description for a given error.
- [func CFErrorCopyRecoverySuggestion(CFError!) -> CFString!](cferrorcopyrecoverysuggestion(_:).md)
  Returns a human presentable recovery suggestion for a given error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cferrorcopyfailurereason(_:))*