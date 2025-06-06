# CFStringEncoding

**Framework**: Core Foundation  
**Kind**: typealias

An integer type for constants used to specify supported string encodings in various CFString functions.

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
typealias CFStringEncoding = UInt32
```

#### Discussion

This type is used to define the constants for the built-in encodings (see [`CFStringBuiltInEncodings`](cfstringbuiltinencodings.md) for a list) and for platform-dependent encodings (see [`External String Encodings`](external-string-encodings.md)). If CFString does not recognize or support the string encoding of a particular string, CFString functions will identify the string’s encoding as [`kCFStringEncodingInvalidId`](kcfstringencodinginvalidid.md).

## See Also

- [enum CFStringEncodings](cfstringencodings.md)
  Index type for constants used to specify external string encodings.
- [struct CFStringCompareFlags](cfstringcompareflags.md)
  A [`CFOptionFlags`](cfoptionflags.md) type for specifying options for string comparison .
- [struct CFStringInlineBuffer](cfstringinlinebuffer.md)
  Defines the buffer and related fields used for in-line buffer access of characters in CFString objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringencoding)*