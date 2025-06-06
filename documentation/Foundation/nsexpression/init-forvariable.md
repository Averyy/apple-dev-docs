# init(forVariable:)

**Framework**: Foundation  
**Kind**: init

Creates an expression that extracts a value from the variable bindings dictionary for a specified key.

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
init(forVariable string: String)
```

#### Return Value

A new expression that extracts from the variable bindings dictionary the value for the key `string`.

## Parameters

- `string`: The key for the variable to extract from the variable bindings dictionary.

## See Also

- [init(forConstantValue: Any?)](nsexpression/init(forconstantvalue:).md)
  Creates an expression that represents a specified constant value.
- [class func expressionForEvaluatedObject() -> NSExpression](nsexpression/expressionforevaluatedobject.md)
  Creates an expression that represents the object you’re evaluating.
- [init(forKeyPath: String)](nsexpression/init(forkeypath:)-1aqf5.md)
  Creates an expression that invokes the value function with a specified key path.
- [convenience init<Root, Value>(forKeyPath: KeyPath<Root, Value>)](nsexpression/init(forkeypath:)-98by.md)
  Creates an expression using a key path you specify.
- [class func expressionForAnyKey() -> NSExpression](nsexpression/expressionforanykey.md)
  Creates an expression that represents any key for a Spotlight query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forvariable:))*