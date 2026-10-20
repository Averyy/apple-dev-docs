# reverseTransformedValue(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the result of the reverse transformation of a given value.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func reverseTransformedValue(_ value: Any?) -> Any?
```

```objc
- (id) reverseTransformedValue:(id) value;
```

#### Return Value

The reverse transformation of `value`.

#### Discussion

The default implementation raises an exception if [`allowsReverseTransformation()`](./allowsreversetransformation%28%29.md) returns [`false`](../../Swift/false.md); otherwise it will invoke [`transformedValue(_:)`](./transformedvalue%28_%29.md) with `value`.

A subclass should override this method if they require a reverse transformation that is not the same as simply reapplying the original transform (as would be the case with negation, for example). For example, if a value transformer converts a value in Fahrenheit to Celsius, this method would converts a value from Celsius to Fahrenheit.

## Parameters

- `value`: The value to reverse transform.

## See Also

### Transforming Values
- [func transformedValue(Any?) -> Any?](./transformedvalue%28_%29.md)
  Returns the result of transforming a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/valuetransformer/reversetransformedvalue(_:))*