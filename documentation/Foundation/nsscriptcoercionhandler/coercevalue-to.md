# coerceValue(_:to:)

**Framework**: Foundation  
**Kind**: method

Returns an object of a given class representing a given value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func coerceValue(_ value: Any, to toClass: AnyClass) -> Any?
```

#### Return Value

An object of the class `toClass` representing the value specified by `value`. Returns `nil` if an error occurs.

## Parameters

- `value`: The value to coerce.
- `toClass`: The class with which to represent  .

## See Also

- [func registerCoercer(Any, selector: Selector, toConvertFrom: AnyClass, to: AnyClass)](nsscriptcoercionhandler/registercoercer(_:selector:toconvertfrom:to:).md)
  Registers a given object (typically a class) to handle coercions (conversions) from one given class to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcoercionhandler/coercevalue(_:to:))*