# init(forConstantValue:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an expression that represents a specified constant value.

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
init(forConstantValue obj: Any?)
```

```objc
+ (NSExpression *) expressionForConstantValue:(id) obj;
```

#### Return Value

A new expression that represents the constant value, `obj`.

## Parameters

- `obj`: The constant value the new expression is to represent.

## See Also

### Creating an Expression for a Value
- [class func expressionForEvaluatedObject() -> NSExpression](./expressionforevaluatedobject%28%29.md)
  Creates an expression that represents the object you’re evaluating.
- [init(forKeyPath: String)](./init%28forkeypath%29-1aqf5.md)
  Creates an expression that invokes the value function with a specified key path.
- [init(forVariable: String)](./init%28forvariable%29.md)
  Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [convenience init<Root, Value>(forKeyPath: KeyPath<Root, Value>)](./init%28forkeypath%29-98by.md)
  Creates an expression using a key path you specify.
- [class func expressionForAnyKey() -> NSExpression](./expressionforanykey%28%29.md)
  Creates an expression that represents any key for a Spotlight query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forconstantvalue:))*