# init(forKeyPath:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an expression using a key path you specify.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init<Root, Value>(forKeyPath keyPath: KeyPath<Root, Value>)
```

## Parameters

- `keyPath`: The key path that the new expression evaluates.

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
- [class func expressionForAnyKey() -> NSExpression](./expressionforanykey%28%29.md)
  Creates an expression that represents any key for a Spotlight query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forkeypath:)-98by)*