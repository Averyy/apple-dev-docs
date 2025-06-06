# withSubstitutionVariables(_:)

**Framework**: Foundation  
**Kind**: method

Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.

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
func withSubstitutionVariables(_ variables: [String : Any]) -> Self
```

#### Return Value

A copy of the receiver with the predicate’s variables substituted by values specified in `variables`.

#### Discussion

The predicate itself is not modified by this method, so you can reuse it for any number of substitutions.

## Parameters

- `variables`: The substitution variables dictionary. The dictionary must contain key-value pairs for all variables in the receiver.

## See Also

- [init(format: String, argumentArray: [Any]?)](nspredicate/init(format:argumentarray:).md)
  Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [init(format: String, arguments: CVaListPointer)](nspredicate/init(format:arguments:).md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [convenience init(format: String, any CVarArg...)](nspredicate/init(format:_:).md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [convenience init?<Input>(Predicate<Input>)](nspredicate/init(_:).md)
  Creates a predicate by converting an existing predicate.
- [init(value: Bool)](nspredicate/init(value:).md)
  Creates and returns a predicate that always evaluates to a specified Boolean value.
- [init(block: (Any?, [String : Any]?) -> Bool)](nspredicate/init(block:).md)
  Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [init?(fromMetadataQueryString: String)](nspredicate/init(frommetadataquerystring:).md)
  Creates a predicate with a metadata query string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/withsubstitutionvariables(_:))*