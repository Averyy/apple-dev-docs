# CFStringGetNameOfEncoding(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the canonical name of a specified string encoding.

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
func CFStringGetNameOfEncoding(_ encoding: CFStringEncoding) -> CFString!
```

#### Return Value

Name of `encoding`; non-localized. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

This function returns the “canonical” name of the string encoding because the return value has to be the same no matter what localization is chosen. In other words, it can’t change based on the International Preferences language panel setting. The canonical name is usually expressed in English.

## Parameters

- `encoding`: The string encoding to use.

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
- [func CFStringGetSmallestEncoding(CFString!) -> CFStringEncoding](cfstringgetsmallestencoding(_:).md)
  Returns the smallest encoding on the current system for the character contents of a string.
- [func CFStringGetSystemEncoding() -> CFStringEncoding](cfstringgetsystemencoding().md)
  Returns the default encoding used by the operating system when it creates strings.
- [func CFStringIsEncodingAvailable(CFStringEncoding) -> Bool](cfstringisencodingavailable(_:).md)
  Determines whether a given Core Foundation string encoding is available on the current system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetnameofencoding(_:))*