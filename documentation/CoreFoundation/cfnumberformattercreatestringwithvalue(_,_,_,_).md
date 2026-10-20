# CFNumberFormatterCreateStringWithValue(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a string representation of the given number or value using the specified number formatter.

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
func CFNumberFormatterCreateStringWithValue(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ numberType: CFNumberType, _ valuePtr: UnsafeRawPointer!) -> CFString!
```

```c
extern CFStringRefCFNumberFormatterCreateStringWithValue(CFAllocatorRef allocator, CFNumberFormatterRef formatter, CFNumberType numberType, const void *valuePtr);
```

#### Return Value

A new string that represents the given number or value formatted by `formatter`. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `formatter`: The number formatter to use.
- `numberType`: The type of value that `valuePtr` references. Valid values are listed in [`CFNumberType`](./cfnumbertype.md).
- `valuePtr`: A pointer to the value to be converted.

## See Also

### Formatting Values
- [func CFNumberFormatterCreateNumberFromString(CFAllocator!, CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFOptionFlags) -> CFNumber!](./cfnumberformattercreatenumberfromstring%28_,_,_,_,_%29.md)
  Returns a number object representing a given string.
- [func CFNumberFormatterCreateStringWithNumber(CFAllocator!, CFNumberFormatter!, CFNumber!) -> CFString!](./cfnumberformattercreatestringwithnumber%28_,_,_%29.md)
  Returns a string representation of the given number using the specified number formatter.
- [func CFNumberFormatterGetDecimalInfoForCurrencyCode(CFString!, UnsafeMutablePointer<Int32>!, UnsafeMutablePointer<Double>!) -> Bool](./cfnumberformattergetdecimalinfoforcurrencycode%28_,_,_%29.md)
  Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.
- [func CFNumberFormatterGetValueFromString(CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFNumberType, UnsafeMutableRawPointer!) -> Bool](./cfnumberformattergetvaluefromstring%28_,_,_,_,_%29.md)
  Returns a number or value representing a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattercreatestringwithvalue(_:_:_:_:))*