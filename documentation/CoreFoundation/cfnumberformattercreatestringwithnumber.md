# CFNumberFormatterCreateStringWithNumber(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a string representation of the given number using the specified number formatter.

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
func CFNumberFormatterCreateStringWithNumber(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ number: CFNumber!) -> CFString!
```

#### Return Value

A new string that represents the given number in the specified format. Returns `NULL` if there was a problem creating the string. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `formatter`: The number formatter to use.
- `number`: The number from which to create a string representation.

## See Also

- [func CFNumberFormatterCreateNumberFromString(CFAllocator!, CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFOptionFlags) -> CFNumber!](cfnumberformattercreatenumberfromstring(_:_:_:_:_:).md)
  Returns a number object representing a given string.
- [func CFNumberFormatterCreateStringWithValue(CFAllocator!, CFNumberFormatter!, CFNumberType, UnsafeRawPointer!) -> CFString!](cfnumberformattercreatestringwithvalue(_:_:_:_:).md)
  Returns a string representation of the given number or value using the specified number formatter.
- [func CFNumberFormatterGetDecimalInfoForCurrencyCode(CFString!, UnsafeMutablePointer<Int32>!, UnsafeMutablePointer<Double>!) -> Bool](cfnumberformattergetdecimalinfoforcurrencycode(_:_:_:).md)
  Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.
- [func CFNumberFormatterGetValueFromString(CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFNumberType, UnsafeMutableRawPointer!) -> Bool](cfnumberformattergetvaluefromstring(_:_:_:_:_:).md)
  Returns a number or value representing a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattercreatestringwithnumber(_:_:_:))*