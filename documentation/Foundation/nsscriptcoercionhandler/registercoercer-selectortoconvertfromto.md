# registerCoercer(_:selector:toConvertFrom:to:)

**Framework**: Foundation  
**Kind**: method

Registers a given object (typically a class) to handle coercions (conversions) from one given class to another.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func registerCoercer(_ coercer: Any, selector: Selector, toConvertFrom fromClass: AnyClass, to toClass: AnyClass)
```

## Parameters

- `coercer`: The object that performs the coercion.   should typically be a class object.
- `selector`: A selector that specifies the method to perform the coercion.   should typically be a factory method, and must take two arguments. The first is the value to be converted. The second is the class to convert it to.
- `fromClass`: The class for which instances are coerced.
- `toClass`: The class to which instances of   are coerced.

## See Also

- [func coerceValue(Any, to: AnyClass) -> Any?](nsscriptcoercionhandler/coercevalue(_:to:).md)
  Returns an object of a given class representing a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcoercionhandler/registercoercer(_:selector:toconvertfrom:to:))*