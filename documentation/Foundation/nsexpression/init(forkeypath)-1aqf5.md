# init(forKeyPath:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an expression that invokes the value function with a specified key path.

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
init(forKeyPath keyPath: String)
```

```objc
+ (NSExpression *) expressionForKeyPath:(NSString *) keyPath;
```

## Return Value

A new expression that invokes [`value(forKeyPath:)`](../../ObjectiveC/nsobject-swift.class/value%28forkeypath%29.md) with `keyPath`.

## Parameters

- `keyPath`: The key path that the new expression should evaluate.

## See Also

### Creating an Expression for a Value
- [init(forConstantValue: Any?)](./init%28forconstantvalue%29.md)
  Creates an expression that represents a specified constant value.
- [class func expressionForEvaluatedObject() -> NSExpression](./expressionforevaluatedobject%28%29.md)
  Creates an expression that represents the object you’re evaluating.
- [init(forVariable: String)](./init%28forvariable%29.md)
  Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [convenience init<Root, Value>(forKeyPath: KeyPath<Root, Value>)](./init%28forkeypath%29-98by.md)
  Creates an expression using a key path you specify.
- [class func expressionForAnyKey() -> NSExpression](./expressionforanykey%28%29.md)
  Creates an expression that represents any key for a Spotlight query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forkeypath:)-1aqf5)*