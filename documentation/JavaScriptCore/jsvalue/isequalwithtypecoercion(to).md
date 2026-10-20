# isEqualWithTypeCoercion(to:)

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Compares the value to another for equivalence, allowing type conversion.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func isEqualWithTypeCoercion(to value: Any!) -> Bool
```

```objc
- (BOOL) isEqualWithTypeCoercionToObject:(id) value;
```

#### Return Value

[`true`](../../Swift/true.md) if the values are equivalent; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method is analogous to the equality operator `==` in JavaScript: it first converts its operands to the same type (if they are not already of the same type), then applies a strict equality comparison to the result. JavaScript object values are equal if and only if they refer to the same object instance.

## Parameters

- `value`: The value to be compared against.

## See Also

### Comparing JavaScript Values
- [func isEqual(to: Any!) -> Bool](./isequal%28to%29.md)
  Compares the value to another for strict equality.
- [func isInstance(of: Any!) -> Bool](./isinstance%28of%29.md)
  Returns a Boolean value indicating whether the value is an instance of another JavaScript object value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/isequalwithtypecoercion(to:))*