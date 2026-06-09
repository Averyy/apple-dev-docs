# makeExpression()

**Framework**: Swift  
**Kind**: method

Creates a pending expression of an array of intent values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func makeExpression() -> IntentValueExpression
```

#### Return Value

An intent value expression representing this array.

#### Discussion

The system evaluates the expression when needed, allowing for lazy conversion of the array’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/makeexpression())*