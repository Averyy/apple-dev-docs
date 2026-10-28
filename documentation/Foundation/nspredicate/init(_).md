# init(_:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a predicate by converting an existing predicate.

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
convenience init?<Input>(_ predicate: Predicate<Input>) where Input : NSObject
```

## Return Value

The converted predicate, or `nil` if conversion fails.

## Discussion

Only a subset of predicates that can be expressed by [`Predicate`](../predicate.md) are convertible to [`NSPredicate`](../nspredicate.md). Predicates that include operations like the following can’t be converted:

- Accessing key paths for properties that aren’t exposed to the Objective-C runtime.
- Capturing values of types that aren’t supported by `NSPredicate`, like custom Swift structures.
- Using some functions or operators, like performing collection operations on a nonstring value.

## Parameters

- `predicate`: The predicate to convert.

## See Also

### Creating a Predicate
- [init(format: String, argumentArray: [Any]?)](./init%28format,argumentarray%29.md)
  Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [init(format: String, arguments: CVaListPointer)](./init%28format,arguments%29.md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [convenience init(format: String, any CVarArg...)](./init%28format,_%29.md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [func withSubstitutionVariables([String : Any]) -> Self](./withsubstitutionvariables%28_%29.md)
  Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [init(value: Bool)](./init%28value%29.md)
  Creates and returns a predicate that always evaluates to a specified Boolean value.
- [init(block: (Any?, [String : Any]?) -> Bool)](./init%28block%29.md)
  Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [init?(fromMetadataQueryString: String)](./init%28frommetadataquerystring%29.md)
  Creates a predicate with a metadata query string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/init(_:))*