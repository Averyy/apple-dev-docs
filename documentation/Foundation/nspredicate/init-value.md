# init(value:)

**Framework**: Foundation  
**Kind**: init

Creates and returns a predicate that always evaluates to a specified Boolean value.

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
init(value: Bool)
```

#### Return Value

A predicate that always evaluates to `value`.

## Parameters

- `value`: The Boolean value to which the new predicate should evaluate.

## See Also

- [init(format: String, argumentArray: [Any]?)](nspredicate/init(format:argumentarray:).md)
  Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [init(format: String, arguments: CVaListPointer)](nspredicate/init(format:arguments:).md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [convenience init(format: String, any CVarArg...)](nspredicate/init(format:_:).md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [convenience init?<Input>(Predicate<Input>)](nspredicate/init(_:).md)
  Creates a predicate by converting an existing predicate.
- [func withSubstitutionVariables([String : Any]) -> Self](nspredicate/withsubstitutionvariables(_:).md)
  Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [init(block: (Any?, [String : Any]?) -> Bool)](nspredicate/init(block:).md)
  Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [init?(fromMetadataQueryString: String)](nspredicate/init(frommetadataquerystring:).md)
  Creates a predicate with a metadata query string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/init(value:))*