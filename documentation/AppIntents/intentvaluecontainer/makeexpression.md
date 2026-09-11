# makeExpression()

**Framework**: App Intents  
**Kind**: method

Creates an intent value expression that represents this container.

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

An intent value expression representing this container.

#### Discussion

This method creates an expression that wraps this container directly, allowing for lazy evaluation during the conversion process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvaluecontainer/makeexpression())*