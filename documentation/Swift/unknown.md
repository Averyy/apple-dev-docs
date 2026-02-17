# !==(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two references point to different object instances.

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
func !== (lhs: AnyObject?, rhs: AnyObject?) -> Bool
```

#### Discussion

This operator tests whether two instances have different identities, not different values. For value inequality, see the not-equal-to operator (`!=`) and the `Equatable` protocol.

## Parameters

- `lhs`: A reference to compare.
- `rhs`: Another reference to compare.

## See Also

- [func === (AnyObject?, AnyObject?) -> Bool](===(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/!==(_:_:))*