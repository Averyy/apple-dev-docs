# transformedValue(_:)

**Framework**: Foundation  
**Kind**: method

Returns the result of transforming a given value.

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
func transformedValue(_ value: Any?) -> Any?
```

#### Return Value

The result of transforming `value`.

The default implementation simply returns `value`.

#### Discussion

A subclass should override this method to transform and return an object based on `value`.

## Parameters

- `value`: The value to transform.

## See Also

- [func reverseTransformedValue(Any?) -> Any?](valuetransformer/reversetransformedvalue(_:).md)
  Returns the result of the reverse transformation of a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/valuetransformer/transformedvalue(_:))*