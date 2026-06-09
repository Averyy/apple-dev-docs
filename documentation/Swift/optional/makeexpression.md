# makeExpression()

**Framework**: Swift  
**Kind**: method

Creates an expression that represents this optional intent value.

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

An intent value expression representing this optional value.

#### Discussion

This method handles both the `.some` and `.none` cases:

- For `.none`, it creates a pending expression that will resolve to a null value
- For `.some`, it delegates to the wrapped value’s expression creation


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/makeexpression())*