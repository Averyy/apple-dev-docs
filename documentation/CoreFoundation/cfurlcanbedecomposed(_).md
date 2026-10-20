# CFURLCanBeDecomposed(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Determines if the given URL conforms to RFC 1808 and therefore can be decomposed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFURLCanBeDecomposed(_ anURL: CFURL!) -> Bool
```

```c
extern Boolean CFURLCanBeDecomposed(CFURLRef anURL);
```

#### Return Value

`true` if `anURL` conforms to RFC 1808, `false` otherwise.

#### Discussion

If a `CFURL` object can be decomposed, you can retrieve separately each of the four components (scheme, net location, path, and resource specifier), as well as the base URL.

Relative URLs are permitted to have only paths (or a variety of other configurations); these are considered decomposable if their base URL is decomposable. If no base URL is present, they are considered decomposable.

## Parameters

- `anURL`: The `CFURL` object to test.

## See Also

### Accessing the Parts of a URL
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
- [func CFURLCopyParameterString(CFURL!, CFString!) -> CFString!](./cfurlcopyparameterstring%28_,_%29.md)
  Returns the parameter string from a given URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcanbedecomposed(_:))*