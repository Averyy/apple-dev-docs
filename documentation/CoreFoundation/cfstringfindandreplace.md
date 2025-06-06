# CFStringFindAndReplace(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Replaces all occurrences of a substring within a given range.

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
func CFStringFindAndReplace(_ theString: CFMutableString!, _ stringToFind: CFString!, _ replacementString: CFString!, _ rangeToSearch: CFRange, _ compareOptions: CFStringCompareFlags) -> CFIndex
```

#### Return Value

The number of instances of `stringToFind` that were replaced.

#### Discussion

The possible values of `compareOptions` are combinations of the [`compareCaseInsensitive`](cfstringcompareflags/comparecaseinsensitive.md), [`compareBackwards`](cfstringcompareflags/comparebackwards.md), [`compareNonliteral`](cfstringcompareflags/comparenonliteral.md), and [`compareAnchored`](cfstringcompareflags/compareanchored.md) constants.

The `kCFCompareBackwards` option can be used to replace a substring starting from the end, which could produce different results. For example, if the parameter `theString` is “AAAAA”, `stringToFind` is “AA”, and `replacementString` is “B”, then the result is normally “BBA”. However, if the `kCFCompareBackwards` constant is used, the result is “ABB.”

The `kCFCompareAnchored` option assures that only anchored but multiple instances are found (the instances must be consecutive at start or end). For example, if the parameter `theString` is “AAXAA”, `stringToFind` is “A”, and `replacementString` is “B”, then the result is normally “BBXBB.” However, if the `kCFCompareAnchored` constant is used, the result is “BBXAA.”

## Parameters

- `theString`: The string to modify.
- `stringToFind`: The substring to search for in  .
- `replacementString`: The replacement string for  .
- `rangeToSearch`: The range within which to search in  .
- `compareOptions`: Flags that select different types of comparisons, such as localized comparison, case-insensitive comparison, and non-literal comparison. If you want the default comparison behavior, pass  . See   for the available flags.

## See Also

- [func CFStringAppend(CFMutableString!, CFString!)](cfstringappend(_:_:).md)
  Appends the characters of a string to those of a CFMutableString object.
- [func CFStringAppendCharacters(CFMutableString!, UnsafePointer<UniChar>!, CFIndex)](cfstringappendcharacters(_:_:_:).md)
  Appends a buffer of Unicode characters to the character contents of a CFMutableString object.
- [func CFStringAppendCString(CFMutableString!, UnsafePointer<CChar>!, CFStringEncoding)](cfstringappendcstring(_:_:_:).md)
  Appends a C string to the character contents of a CFMutableString object.
- [func CFStringAppendFormatAndArguments(CFMutableString!, CFDictionary!, CFString!, CVaListPointer)](cfstringappendformatandarguments(_:_:_:_:).md)
  Appends a formatted string to the character contents of a CFMutableString object.
- [func CFStringAppendPascalString(CFMutableString!, ConstStr255Param!, CFStringEncoding)](cfstringappendpascalstring(_:_:_:).md)
  Appends a Pascal string to the character contents of a CFMutableString object.
- [func CFStringCapitalize(CFMutableString!, CFLocale!)](cfstringcapitalize(_:_:).md)
  Changes the first character in each word of a string to uppercase (if it is a lowercase alphabetical character).
- [func CFStringCreateMutable(CFAllocator!, CFIndex) -> CFMutableString!](cfstringcreatemutable(_:_:).md)
  Creates an empty CFMutableString object.
- [func CFStringCreateMutableCopy(CFAllocator!, CFIndex, CFString!) -> CFMutableString!](cfstringcreatemutablecopy(_:_:_:).md)
  Creates a mutable copy of a string.
- [func CFStringCreateMutableWithExternalCharactersNoCopy(CFAllocator!, UnsafeMutablePointer<UniChar>!, CFIndex, CFIndex, CFAllocator!) -> CFMutableString!](cfstringcreatemutablewithexternalcharactersnocopy(_:_:_:_:_:).md)
  Creates a CFMutableString object whose Unicode character buffer is controlled externally.
- [func CFStringDelete(CFMutableString!, CFRange)](cfstringdelete(_:_:).md)
  Deletes a range of characters in a string.
- [func CFStringFold(CFMutableString!, CFStringCompareFlags, CFLocale!)](cfstringfold(_:_:_:).md)
  Folds a given string into the form specified by optional flags.
- [func CFStringInsert(CFMutableString!, CFIndex, CFString!)](cfstringinsert(_:_:_:).md)
  Inserts a string at a specified location in the character buffer of a CFMutableString object.
- [func CFStringLowercase(CFMutableString!, CFLocale!)](cfstringlowercase(_:_:).md)
  Changes all uppercase alphabetical characters in a CFMutableString to lowercase.
- [func CFStringNormalize(CFMutableString!, CFStringNormalizationForm)](cfstringnormalize(_:_:).md)
  Normalizes the string into the specified form as described in Unicode Technical Report #15.
- [func CFStringPad(CFMutableString!, CFString!, CFIndex, CFIndex)](cfstringpad(_:_:_:_:).md)
  Enlarges a string, padding it with specified characters, or truncates the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringfindandreplace(_:_:_:_:_:))*