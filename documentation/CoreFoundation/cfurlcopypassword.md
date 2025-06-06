# CFURLCopyPassword(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the password of a given URL.

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
func CFURLCopyPassword(_ anURL: CFURL!) -> CFString!
```

#### Return Value

The password, or `NULL` if no password exists. In some cases, this function may also return the empty string (`CFSTR("")`) if no password exists. You should consider `NULL` and the empty string to be equivalent. Ownership follows the create rule. See [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `anURL`: The   object to examine.

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
- [func CFURLCopyParameterString(CFURL!, CFString!) -> CFString!](cfurlcopyparameterstring(_:_:).md)
  Returns the parameter string from a given URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcopypassword(_:))*