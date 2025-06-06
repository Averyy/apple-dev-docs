# CFNumberFormatterCreateNumberFromString(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a number object representing a given string.

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
func CFNumberFormatterCreateNumberFromString(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!, _ options: CFOptionFlags) -> CFNumber!
```

#### Return Value

A new number that represents the given string. Returns `NULL` if there was a problem creating the number. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `formatter`: The number formatter to use.
- `string`: The string to parse.
- `rangep`: A reference to a range that specifies the substring of    to be parsed. If  , the whole string is parsed. On return, contains the range of the actual extent of the parse (may be less than the given range).
- `options`: Specifies various configuration options to change the behavior of the parse. Currently,   is the only possible value for this parameter.

## See Also

- [func CFNumberFormatterCreateStringWithNumber(CFAllocator!, CFNumberFormatter!, CFNumber!) -> CFString!](cfnumberformattercreatestringwithnumber(_:_:_:).md)
  Returns a string representation of the given number using the specified number formatter.
- [func CFNumberFormatterCreateStringWithValue(CFAllocator!, CFNumberFormatter!, CFNumberType, UnsafeRawPointer!) -> CFString!](cfnumberformattercreatestringwithvalue(_:_:_:_:).md)
  Returns a string representation of the given number or value using the specified number formatter.
- [func CFNumberFormatterGetDecimalInfoForCurrencyCode(CFString!, UnsafeMutablePointer<Int32>!, UnsafeMutablePointer<Double>!) -> Bool](cfnumberformattergetdecimalinfoforcurrencycode(_:_:_:).md)
  Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.
- [func CFNumberFormatterGetValueFromString(CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFNumberType, UnsafeMutableRawPointer!) -> Bool](cfnumberformattergetvaluefromstring(_:_:_:_:_:).md)
  Returns a number or value representing a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattercreatenumberfromstring(_:_:_:_:_:))*