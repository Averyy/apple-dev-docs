# isInstance(of:)

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the value is an instance of another JavaScript object value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func isInstance(of value: Any!) -> Bool
```

```objc
- (BOOL) isInstanceOf:(id) value;
```

#### Return Value

[`true`](../../Swift/true.md) if this value inherits from `value`; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method is analogous to the `instanceof` operator in JavaScript: it tests for the presence of the specified value’s constructor prototype in this value’s prototype chain.

## Parameters

- `value`: The value to be compared against.

## See Also

### Comparing JavaScript Values
- [func isEqual(to: Any!) -> Bool](./isequal%28to%29.md)
  Compares the value to another for strict equality.
- [func isEqualWithTypeCoercion(to: Any!) -> Bool](./isequalwithtypecoercion%28to%29.md)
  Compares the value to another for equivalence, allowing type conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/isinstance(of:))*