# init(block:arguments:)

**Framework**: Foundation  
**Kind**: init

Creates an expression object that uses the block for evaluating objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(block: @escaping (Any?, [NSExpression], NSMutableDictionary?) -> Any, arguments: [NSExpression]?)
```

#### Return Value

An expression that filters a collection using the specified Block.

## Parameters

- `block`: The Block is applied to the object to be evaluated. The Block takes three arguments and returns a value: - **evaluatedObject**: The object to be evaluated.
- **expressions**: An array of predicate expressions that evaluates to a collection.
- **context**: A dictionary that the expression can use to store temporary state for one predicate evaluation. Note that `context` is mutable, and that it can only be accessed during the evaluation of the expression. You must not attempt to retain it for use elsewhere. ] The Block returns the `evaluatedObject`.
- `arguments`: An array containing `NSExpression` objects that will be used as parameters during the invocation of selector. For a selector taking no parameters, the array should be empty. For a selector taking one or more parameters, the array should contain one `NSExpression` object which will evaluate to an instance of the appropriate type for each parameter. If there is a mismatch between the number of parameters expected and the number you provide during evaluation, an exception may be raised or missing parameters may simply be replaced by `nil` (which occurs depends on how many parameters are provided, and whether you have over- or underflow). See [`init(forFunction:arguments:)`](nsexpression/init(forfunction:arguments:).md) for a complete list of arguments.

## See Also

- [var expressionBlock: (Any?, [NSExpression], NSMutableDictionary?) -> Any](nsexpression/expressionblock.md)
  The block that executes to evaluate the expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(block:arguments:))*