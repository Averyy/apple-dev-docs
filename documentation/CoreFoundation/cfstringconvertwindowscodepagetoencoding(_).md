# CFStringConvertWindowsCodepageToEncoding(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the Core Foundation encoding constant that is the closest mapping to a given Windows codepage identifier.

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
func CFStringConvertWindowsCodepageToEncoding(_ codepage: UInt32) -> CFStringEncoding
```

```c
extern CFStringEncoding CFStringConvertWindowsCodepageToEncoding(UInt32 codepage);
```

## Return Value

The Core Foundation string encoding that is closest to the Windows codepage identifier `codepage`. Returns the [`kCFStringEncodingInvalidId`](./kcfstringencodinginvalidid.md) constant if the mapping is not known.

## Discussion

The [`CFStringConvertEncodingToWindowsCodepage(_:)`](./cfstringconvertencodingtowindowscodepage%28_%29.md) function is complementary to this function.

## Parameters

- `codepage`: The Windows codepage identifier to use.

## See Also

### Working With Encodings
- [func CFStringConvertEncodingToIANACharSetName(CFStringEncoding) -> CFString!](./cfstringconvertencodingtoianacharsetname%28_%29.md)
  Returns the name of the IANA registry “charset” that is the closest mapping to a specified string encoding.
- [func CFStringConvertEncodingToNSStringEncoding(CFStringEncoding) -> UInt](./cfstringconvertencodingtonsstringencoding%28_%29.md)
  Returns the Cocoa encoding constant that maps most closely to a given Core Foundation encoding constant.
- [func CFStringConvertEncodingToWindowsCodepage(CFStringEncoding) -> UInt32](./cfstringconvertencodingtowindowscodepage%28_%29.md)
  Returns the Windows codepage identifier that maps most closely to a given Core Foundation encoding constant.
- [func CFStringConvertIANACharSetNameToEncoding(CFString!) -> CFStringEncoding](./cfstringconvertianacharsetnametoencoding%28_%29.md)
  Returns the Core Foundation encoding constant that is the closest mapping to a given IANA registry “charset” name.
- [func CFStringConvertNSStringEncodingToEncoding(UInt) -> CFStringEncoding](./cfstringconvertnsstringencodingtoencoding%28_%29.md)
  Returns the Core Foundation encoding constant that is the closest mapping to a given Cocoa encoding.
- [func CFStringGetFastestEncoding(CFString!) -> CFStringEncoding](./cfstringgetfastestencoding%28_%29.md)
  Returns for a CFString object the character encoding that requires the least conversion time.
- [func CFStringGetListOfAvailableEncodings() -> UnsafePointer<CFStringEncoding>!](./cfstringgetlistofavailableencodings%28%29.md)
  Returns a pointer to a list of string encodings supported by the current system.
- [func CFStringGetMaximumSizeForEncoding(CFIndex, CFStringEncoding) -> CFIndex](./cfstringgetmaximumsizeforencoding%28_,_%29.md)
  Returns the maximum number of bytes a string of a specified length (in Unicode characters) will take up if encoded in a specified encoding.
- [func CFStringGetMostCompatibleMacStringEncoding(CFStringEncoding) -> CFStringEncoding](./cfstringgetmostcompatiblemacstringencoding%28_%29.md)
  Returns the most compatible Mac OS script value for the given input encoding.
- [func CFStringGetNameOfEncoding(CFStringEncoding) -> CFString!](./cfstringgetnameofencoding%28_%29.md)
  Returns the canonical name of a specified string encoding.
- [func CFStringGetSmallestEncoding(CFString!) -> CFStringEncoding](./cfstringgetsmallestencoding%28_%29.md)
  Returns the smallest encoding on the current system for the character contents of a string.
- [func CFStringGetSystemEncoding() -> CFStringEncoding](./cfstringgetsystemencoding%28%29.md)
  Returns the default encoding used by the operating system when it creates strings.
- [func CFStringIsEncodingAvailable(CFStringEncoding) -> Bool](./cfstringisencodingavailable%28_%29.md)
  Determines whether a given Core Foundation string encoding is available on the current system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringconvertwindowscodepagetoencoding(_:))*