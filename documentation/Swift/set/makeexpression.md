# makeExpression()

**Framework**: Swift  
**Kind**: method

Creates a pending expression of a set of intent values.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func makeExpression() -> IntentValueExpression
```

#### Return Value

An intent value expression representing this set.

#### Discussion

The system evaluates the expression when needed, allowing for lazy conversion of the set’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/makeexpression())*