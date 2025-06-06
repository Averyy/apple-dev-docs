# CFURLCopyParameterString(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the parameter string from a given URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLCopyParameterString(_ anURL: CFURL!, _ charactersToLeaveEscaped: CFString!) -> CFString!
```

#### Return Value

The parameter string (as defined in RFC 1738), or `NULL` if no parameter string exists. For example, in the URL `myproto://www.example.com/;command=laugh`, the parameter string is `command=laugh`. Ownership follows the create rule. See [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function removes all percent escape sequences except those for characters specified in `charactersToLeaveEscaped`.

## Parameters

- `anURL`: The   object to examine.
- `charactersToLeaveEscaped`: Characters whose percent escape sequences, such as   for a space character, you want to leave intact. Pass   to specify that no percent escapes be replaced, or the empty string ( ) to specify that all be replaced.

## See Also

- [func CFURLCanBeDecomposed(CFURL!) -> Bool](cfurlcanbedecomposed(_:).md)
  Determines if the given URL conforms to RFC 1808 and therefore can be decomposed.
- [func CFURLCopyFileSystemPath(CFURL!, CFURLPathStyle) -> CFString!](cfurlcopyfilesystempath(_:_:).md)
  Returns the path portion of a given URL.
- [func CFURLCopyFragment(CFURL!, CFString!) -> CFString!](cfurlcopyfragment(_:_:).md)
  Returns the fragment from a given URL.
- [func CFURLCopyHostName(CFURL!) -> CFString!](cfurlcopyhostname(_:).md)
  Returns the host name of a given URL.
- [func CFURLCopyLastPathComponent(CFURL!) -> CFString!](cfurlcopylastpathcomponent(_:).md)
  Returns the last path component of a given URL.
- [func CFURLCopyNetLocation(CFURL!) -> CFString!](cfurlcopynetlocation(_:).md)
  Returns the net location portion of a given URL.
- [func CFURLCopyPassword(CFURL!) -> CFString!](cfurlcopypassword(_:).md)
  Returns the password of a given URL.
- [func CFURLCopyPath(CFURL!) -> CFString!](cfurlcopypath(_:).md)
  Returns the path portion of a given URL.
- [func CFURLCopyPathExtension(CFURL!) -> CFString!](cfurlcopypathextension(_:).md)
  Returns the path extension of a given URL.
- [func CFURLCopyQueryString(CFURL!, CFString!) -> CFString!](cfurlcopyquerystring(_:_:).md)
  Returns the query string of a given URL.
- [func CFURLCopyResourceSpecifier(CFURL!) -> CFString!](cfurlcopyresourcespecifier(_:).md)
  Returns any additional resource specifiers after the path.
- [func CFURLCopyScheme(CFURL!) -> CFString!](cfurlcopyscheme(_:).md)
  Returns the scheme portion of a given URL.
- [func CFURLCopyStrictPath(CFURL!, UnsafeMutablePointer<DarwinBoolean>!) -> CFString!](cfurlcopystrictpath(_:_:).md)
  Returns the path portion of a given URL.
- [func CFURLCopyUserName(CFURL!) -> CFString!](cfurlcopyusername(_:).md)
  Returns the user name from a given URL.
- [func CFURLGetPortNumber(CFURL!) -> Int32](cfurlgetportnumber(_:).md)
  Returns the port number from a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcopyparameterstring(_:_:))*