# init(forFunction:selectorName:arguments:)

**Framework**: Foundation  
**Kind**: init

Creates an expression that returns the result of invoking a selector with a specified name using specified arguments.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(forFunction target: NSExpression, selectorName name: String, arguments parameters: [Any]?)
```

#### Return Value

An expression which will return the result of invoking the selector named `name` on the result of evaluating the target expression with the parameters specified by evaluating the elements of `parameters`.

#### Discussion

See the description of [`init(forFunction:arguments:)`](nsexpression/init(forfunction:arguments:).md) for examples of how to construct the parameter array.

##### Special Considerations

This method throws an exception immediately if the selector is unknown; it throws at runtime if the parameters are incorrect.

This expression effectively allows your application to invoke any method on any object it can navigate to at runtime. You must consider the security implications of this type of evaluation.

## Parameters

- `target`: An   object which will evaluate an object on which the selector identified by   may be invoked.
- `name`: The name of the method to be invoked.
- `parameters`: An array containing   objects which can be evaluated to provide parameters for the method specified by  .

## See Also

- [init(forFunction: String, arguments: [Any])](nsexpression/init(forfunction:arguments:).md)
  Creates an expression that invokes one of the predefined functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forfunction:selectorname:arguments:))*