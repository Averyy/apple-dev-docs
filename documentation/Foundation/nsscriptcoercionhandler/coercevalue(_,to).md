# coerceValue(_:to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an object of a given class representing a given value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func coerceValue(_ value: Any, to toClass: AnyClass) -> Any?
```

```objc
- (id) coerceValue:(id) value toClass:(Class) toClass;
```

## Return Value

An object of the class `toClass` representing the value specified by `value`. Returns `nil` if an error occurs.

## Parameters

- `value`: The value to coerce.
- `toClass`: The class with which to represent `value`.

## See Also

### Working with handlers
- [func registerCoercer(Any, selector: Selector, toConvertFrom: AnyClass, to: AnyClass)](./registercoercer%28_,selector,toconvertfrom,to%29.md)
  Registers a given object (typically a class) to handle coercions (conversions) from one given class to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcoercionhandler/coercevalue(_:to:))*