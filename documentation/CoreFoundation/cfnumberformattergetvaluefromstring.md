# CFNumberFormatterGetValueFromString(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a number or value representing a given string.

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
func CFNumberFormatterGetValueFromString(_ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!, _ numberType: CFNumberType, _ valuePtr: UnsafeMutableRawPointer!) -> Bool
```

#### Return Value

`true` if the string was parsed successfully, otherwise `false`.

## Parameters

- `formatter`: The number formatter to use.
- `string`: The string to parse.
- `rangep`: A reference to a range that specifies the substring of    to be parsed. If  , the whole string is parsed. Upon return, contains the range of the actual extent of the parse (may be less than the given range).
- `numberType`: The type of value that   references. Valid values are listed in  .
- `valuePtr`: Upon return, contains a number or value representing the string in the specified format. You are responsible for releasing this value.

## See Also

- [func CFNumberFormatterCreateNumberFromString(CFAllocator!, CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFOptionFlags) -> CFNumber!](cfnumberformattercreatenumberfromstring(_:_:_:_:_:).md)
  Returns a number object representing a given string.
- [func CFNumberFormatterCreateStringWithNumber(CFAllocator!, CFNumberFormatter!, CFNumber!) -> CFString!](cfnumberformattercreatestringwithnumber(_:_:_:).md)
  Returns a string representation of the given number using the specified number formatter.
- [func CFNumberFormatterCreateStringWithValue(CFAllocator!, CFNumberFormatter!, CFNumberType, UnsafeRawPointer!) -> CFString!](cfnumberformattercreatestringwithvalue(_:_:_:_:).md)
  Returns a string representation of the given number or value using the specified number formatter.
- [func CFNumberFormatterGetDecimalInfoForCurrencyCode(CFString!, UnsafeMutablePointer<Int32>!, UnsafeMutablePointer<Double>!) -> Bool](cfnumberformattergetdecimalinfoforcurrencycode(_:_:_:).md)
  Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattergetvaluefromstring(_:_:_:_:_:))*