# isEqual(to:)

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Compares the value to another for strict equality.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func isEqual(to value: Any!) -> Bool
```

```objc
- (BOOL) isEqualToObject:(id) value;
```

#### Return Value

[`true`](../../Swift/true.md) if the values are strictly equal; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method is analogous to the identity or strict equality operator `===` in JavaScript.

## Parameters

- `value`: The value to be compared against.

## See Also

### Comparing JavaScript Values
- [func isEqualWithTypeCoercion(to: Any!) -> Bool](./isequalwithtypecoercion%28to%29.md)
  Compares the value to another for equivalence, allowing type conversion.
- [func isInstance(of: Any!) -> Bool](./isinstance%28of%29.md)
  Returns a Boolean value indicating whether the value is an instance of another JavaScript object value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/isequal(to:))*