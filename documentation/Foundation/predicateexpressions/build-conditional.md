# build_Conditional(_:_:_:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func build_Conditional<Test, If, Else>(_ test: Test, _ trueBranch: If, _ falseBranch: Else) -> PredicateExpressions.Conditional<Test, If, Else> where Test : PredicateExpression, If : PredicateExpression, Else : PredicateExpression, Test.Output == Bool, If.Output == Else.Output
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_conditional(_:_:_:))*