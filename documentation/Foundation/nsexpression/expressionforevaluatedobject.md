# expressionForEvaluatedObject()

**Framework**: Foundation  
**Kind**: method

Creates an expression that represents the object you’re evaluating.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func expressionForEvaluatedObject() -> NSExpression
```

#### Return Value

A new expression that represents the object being evaluated.

## See Also

- [init(forConstantValue: Any?)](nsexpression/init(forconstantvalue:).md)
  Creates an expression that represents a specified constant value.
- [init(forKeyPath: String)](nsexpression/init(forkeypath:)-1aqf5.md)
  Creates an expression that invokes the value function with a specified key path.
- [init(forVariable: String)](nsexpression/init(forvariable:).md)
  Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [convenience init<Root, Value>(forKeyPath: KeyPath<Root, Value>)](nsexpression/init(forkeypath:)-98by.md)
  Creates an expression using a key path you specify.
- [class func expressionForAnyKey() -> NSExpression](nsexpression/expressionforanykey.md)
  Creates an expression that represents any key for a Spotlight query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/expressionforevaluatedobject())*