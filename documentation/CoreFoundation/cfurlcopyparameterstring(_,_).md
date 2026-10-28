# CFURLCopyParameterString(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the parameter string from a given URL.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: The CFURLCopyParameterString function is deprecated. Post deprecation for applications linked with or after the macOS 10.15, and for all iOS, watchOS, and tvOS applications, CFURLCopyParameterString will always return NULL, and the CFURLCopyPath(), CFURLCopyStrictPath(), and CFURLCopyFileSystemPath() functions will return the complete path including the semicolon separator and params component if the URL string contains them.

## Declaration

```swift
func CFURLCopyParameterString(_ anURL: CFURL!, _ charactersToLeaveEscaped: CFString!) -> CFString!
```

```c
extern CFStringRefCFURLCopyParameterString(CFURLRef anURL, CFStringRef charactersToLeaveEscaped);
```

## Return Value

The parameter string (as defined in RFC 1738), or `NULL` if no parameter string exists. For example, in the URL `myproto://www.example.com/;command=laugh`, the parameter string is `command=laugh`. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function removes all percent escape sequences except those for characters specified in `charactersToLeaveEscaped`.

## Parameters

- `anURL`: The `CFURL` object to examine.
- `charactersToLeaveEscaped`: Characters whose percent escape sequences, such as `%20` for a space character, you want to leave intact. Pass `NULL` to specify that no percent escapes be replaced, or the empty string (`CFSTR("")`) to specify that all be replaced.

## See Also

### Accessing the Parts of a URL
- [func CFURLCanBeDecomposed(CFURL!) -> Bool](./cfurlcanbedecomposed%28_%29.md)
  Determines if the given URL conforms to RFC 1808 and therefore can be decomposed.
- [func CFURLCopyFileSystemPath(CFURL!, CFURLPathStyle) -> CFString!](./cfurlcopyfilesystempath%28_,_%29.md)
  Returns the path portion of a given URL.
- [func CFURLCopyFragment(CFURL!, CFString!) -> CFString!](./cfurlcopyfragment%28_,_%29.md)
  Returns the fragment from a given URL.
- [func CFURLCopyHostName(CFURL!) -> CFString!](./cfurlcopyhostname%28_%29.md)
  Returns the host name of a given URL.
- [func CFURLCopyLastPathComponent(CFURL!) -> CFString!](./cfurlcopylastpathcomponent%28_%29.md)
  Returns the last path component of a given URL.
- [func CFURLCopyNetLocation(CFURL!) -> CFString!](./cfurlcopynetlocation%28_%29.md)
  Returns the net location portion of a given URL.
- [func CFURLCopyPassword(CFURL!) -> CFString!](./cfurlcopypassword%28_%29.md)
  Returns the password of a given URL.
- [func CFURLCopyPath(CFURL!) -> CFString!](./cfurlcopypath%28_%29.md)
  Returns the path portion of a given URL.
- [func CFURLCopyPathExtension(CFURL!) -> CFString!](./cfurlcopypathextension%28_%29.md)
  Returns the path extension of a given URL.
- [func CFURLCopyQueryString(CFURL!, CFString!) -> CFString!](./cfurlcopyquerystring%28_,_%29.md)
  Returns the query string of a given URL.
- [func CFURLCopyResourceSpecifier(CFURL!) -> CFString!](./cfurlcopyresourcespecifier%28_%29.md)
  Returns any additional resource specifiers after the path.
- [func CFURLCopyScheme(CFURL!) -> CFString!](./cfurlcopyscheme%28_%29.md)
  Returns the scheme portion of a given URL.
- [func CFURLCopyStrictPath(CFURL!, UnsafeMutablePointer<DarwinBoolean>!) -> CFString!](./cfurlcopystrictpath%28_,_%29.md)
  Returns the path portion of a given URL.
- [func CFURLCopyUserName(CFURL!) -> CFString!](./cfurlcopyusername%28_%29.md)
  Returns the user name from a given URL.
- [func CFURLGetPortNumber(CFURL!) -> Int32](./cfurlgetportnumber%28_%29.md)
  Returns the port number from a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcopyparameterstring(_:_:))*