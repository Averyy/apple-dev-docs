# ==(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns a Boolean value indicating whether two values are equal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static func == (a: Result<Success, Failure>, b: Result<Success, Failure>) -> Bool
```

Available when `Success` conforms to `Equatable`, `Failure` conforms to `Equatable`, and `Failure` conforms to `Error`.

#### Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.

## See Also

### Comparing Results
- [static func != (borrowing Self, borrowing Self) -> Bool](./noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/==(_:_:))*