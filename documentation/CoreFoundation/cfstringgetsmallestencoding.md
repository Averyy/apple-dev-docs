# CFStringGetSmallestEncoding(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the smallest encoding on the current system for the character contents of a string.

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
func CFStringGetSmallestEncoding(_ theString: CFString!) -> CFStringEncoding
```

#### Return Value

The string encoding that has the smallest representation of `theString`.

#### Discussion

This function returns the supported encoding that requires the least space (in terms of bytes needed to represent one character) to represent the character contents of a string. This information is not always immediately available, so this function might need to compute it.

## Parameters

- `theString`: The string for which to find the smallest encoding.

## See Also

- [func CFStringConvertEncodingToIANACharSetName(CFStringEncoding) -> CFString!](cfstringconvertencodingtoianacharsetname(_:).md)
  Returns the name of the IANA registry “charset” that is the closest mapping to a specified string encoding.
- [func CFStringConvertEncodingToNSStringEncoding(CFStringEncoding) -> UInt](cfstringconvertencodingtonsstringencoding(_:).md)
  Returns the Cocoa encoding constant that maps most closely to a given Core Foundation encoding constant.
- [func CFStringConvertEncodingToWindowsCodepage(CFStringEncoding) -> UInt32](cfstringconvertencodingtowindowscodepage(_:).md)
  Returns the Windows codepage identifier that maps most closely to a given Core Foundation encoding constant.
- [func CFStringConvertIANACharSetNameToEncoding(CFString!) -> CFStringEncoding](cfstringconvertianacharsetnametoencoding(_:).md)
  Returns the Core Foundation encoding constant that is the closest mapping to a given IANA registry “charset” name.
- [func CFStringConvertNSStringEncodingToEncoding(UInt) -> CFStringEncoding](cfstringconvertnsstringencodingtoencoding(_:).md)
  Returns the Core Foundation encoding constant that is the closest mapping to a given Cocoa encoding.
- [func CFStringConvertWindowsCodepageToEncoding(UInt32) -> CFStringEncoding](cfstringconvertwindowscodepagetoencoding(_:).md)
  Returns the Core Foundation encoding constant that is the closest mapping to a given Windows codepage identifier.
- [func CFStringGetFastestEncoding(CFString!) -> CFStringEncoding](cfstringgetfastestencoding(_:).md)
  Returns for a CFString object the character encoding that requires the least conversion time.
- [func CFStringGetListOfAvailableEncodings() -> UnsafePointer<CFStringEncoding>!](cfstringgetlistofavailableencodings().md)
  Returns a pointer to a list of string encodings supported by the current system.
- [func CFStringGetMaximumSizeForEncoding(CFIndex, CFStringEncoding) -> CFIndex](cfstringgetmaximumsizeforencoding(_:_:).md)
  Returns the maximum number of bytes a string of a specified length (in Unicode characters) will take up if encoded in a specified encoding.
- [func CFStringGetMostCompatibleMacStringEncoding(CFStringEncoding) -> CFStringEncoding](cfstringgetmostcompatiblemacstringencoding(_:).md)
  Returns the most compatible Mac OS script value for the given input encoding.
- [func CFStringGetNameOfEncoding(CFStringEncoding) -> CFString!](cfstringgetnameofencoding(_:).md)
  Returns the canonical name of a specified string encoding.
- [func CFStringGetSystemEncoding() -> CFStringEncoding](cfstringgetsystemencoding().md)
  Returns the default encoding used by the operating system when it creates strings.
- [func CFStringIsEncodingAvailable(CFStringEncoding) -> Bool](cfstringisencodingavailable(_:).md)
  Determines whether a given Core Foundation string encoding is available on the current system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetsmallestencoding(_:))*