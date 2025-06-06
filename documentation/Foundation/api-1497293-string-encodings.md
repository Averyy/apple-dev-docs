# String Encodings

**Framework**: Foundation

Constants for encoding standards used when converting raw data to and from string representations.

## Topics

### 7- and 8-bit Encodings
- [var NSASCIIStringEncoding: UInt](nsasciistringencoding.md)
  Strict 7-bit ASCII encoding within 8-bit chars; ASCII values 0…127 only.
- [var NSISOLatin1StringEncoding: UInt](nsisolatin1stringencoding.md)
  8-bit ISO Latin 1 encoding.
- [var NSISOLatin2StringEncoding: UInt](nsisolatin2stringencoding.md)
  8-bit ISO Latin 2 encoding.
- [var NSMacOSRomanStringEncoding: UInt](nsmacosromanstringencoding.md)
  Classic Macintosh Roman encoding.
- [var NSNEXTSTEPStringEncoding: UInt](nsnextstepstringencoding.md)
  8-bit ASCII encoding with NEXTSTEP extensions.
- [var NSNonLossyASCIIStringEncoding: UInt](nsnonlossyasciistringencoding.md)
  7-bit verbose ASCII to represent all Unicode characters.
- [var NSSymbolStringEncoding: UInt](nssymbolstringencoding.md)
  8-bit Adobe Symbol encoding vector.
### 7- and 8-bit Japanese Encodings
- [var NSISO2022JPStringEncoding: UInt](nsiso2022jpstringencoding.md)
  ISO 2022 Japanese encoding for email.
- [var NSJapaneseEUCStringEncoding: UInt](nsjapaneseeucstringencoding.md)
  8-bit EUC encoding for Japanese text.
- [var NSShiftJISStringEncoding: UInt](nsshiftjisstringencoding.md)
  8-bit Shift-JIS encoding for Japanese text.
### Unicode Encodings
- [var NSUTF8StringEncoding: UInt](nsutf8stringencoding.md)
  An 8-bit representation of Unicode characters, suitable for transmission or storage by ASCII-based systems.
- [var NSUTF16BigEndianStringEncoding: UInt](nsutf16bigendianstringencoding.md)
  `NSUTF16StringEncoding` encoding with explicit endianness specified.
- [var NSUTF16LittleEndianStringEncoding: UInt](nsutf16littleendianstringencoding.md)
  `NSUTF16StringEncoding` encoding with explicit endianness specified.
- [var NSUTF16StringEncoding: UInt](nsutf16stringencoding.md)
- [var NSUnicodeStringEncoding: UInt](nsunicodestringencoding.md)
  The canonical Unicode encoding for string objects.
- [var NSUTF32BigEndianStringEncoding: UInt](nsutf32bigendianstringencoding.md)
  `NSUTF32StringEncoding` encoding with explicit endianness specified.
- [var NSUTF32LittleEndianStringEncoding: UInt](nsutf32littleendianstringencoding.md)
  `NSUTF32StringEncoding` encoding with explicit endianness specified.
- [var NSUTF32StringEncoding: UInt](nsutf32stringencoding.md)
  32-bit UTF encoding.
### Windows Code Page Encodings
- [var NSWindowsCP1250StringEncoding: UInt](nswindowscp1250stringencoding.md)
  Microsoft Windows codepage 1250; equivalent to WinLatin2.
- [var NSWindowsCP1251StringEncoding: UInt](nswindowscp1251stringencoding.md)
  Microsoft Windows codepage 1251, encoding Cyrillic characters; equivalent to AdobeStandardCyrillic font encoding.
- [var NSWindowsCP1252StringEncoding: UInt](nswindowscp1252stringencoding.md)
  Microsoft Windows codepage 1252; equivalent to WinLatin1.
- [var NSWindowsCP1253StringEncoding: UInt](nswindowscp1253stringencoding.md)
  Microsoft Windows codepage 1253, encoding Greek characters.
- [var NSWindowsCP1254StringEncoding: UInt](nswindowscp1254stringencoding.md)
  Microsoft Windows codepage 1254, encoding Turkish characters.

## See Also

- [@frozen struct String](../Swift/String.md)
  A Unicode string value that is a collection of characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/1497293-string-encodings)*