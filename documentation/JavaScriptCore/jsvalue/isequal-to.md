# isEqual(to:)

**Framework**: JavaScriptCore  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the values are strictly equal; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is analogous to the identity or strict equality operator `===` in JavaScript.

## Parameters

- `value`: The value to be compared against.

## See Also

- [func isEqualWithTypeCoercion(to: Any!) -> Bool](jsvalue/isequalwithtypecoercion(to:).md)
  Compares the value to another for equivalence, allowing type conversion.
- [func isInstance(of: Any!) -> Bool](jsvalue/isinstance(of:).md)
  Returns a Boolean value indicating whether the value is an instance of another JavaScript object value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/isequal(to:))*