# expressionForAnyKey()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an expression that represents any key for a Spotlight query.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func expressionForAnyKey() -> NSExpression
```

```objc
+ (NSExpression *) expressionForAnyKey;
```

## Return Value

A new expression that represents any key for a Spotlight query.

## See Also

### Creating an Expression for a Value
- [init(forConstantValue: Any?)](./init%28forconstantvalue%29.md)
  Creates an expression that represents a specified constant value.
- [class func expressionForEvaluatedObject() -> NSExpression](./expressionforevaluatedobject%28%29.md)
  Creates an expression that represents the object you’re evaluating.
- [init(forKeyPath: String)](./init%28forkeypath%29-1aqf5.md)
  Creates an expression that invokes the value function with a specified key path.
- [init(forVariable: String)](./init%28forvariable%29.md)
  Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [convenience init<Root, Value>(forKeyPath: KeyPath<Root, Value>)](./init%28forkeypath%29-98by.md)
  Creates an expression using a key path you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/expressionforanykey())*