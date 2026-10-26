# withSubstitutionVariables(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (instancetype) predicateWithSubstitutionVariables:(NSDictionary<NSString *,id> *) variables;
```

#### Return Value

A copy of the receiver with the predicate’s variables substituted by values specified in `variables`.

#### Discussion

The predicate itself is not modified by this method, so you can reuse it for any number of substitutions.

## Parameters

- `variables`: The substitution variables dictionary. The dictionary must contain key-value pairs for all variables in the receiver.

## See Also

### Creating a Predicate
- [init(format: String, argumentArray: [Any]?)](./init%28format,argumentarray%29.md)
  Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [init(format: String, arguments: CVaListPointer)](./init%28format,arguments%29.md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [convenience init(format: String, any CVarArg...)](./init%28format,_%29.md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [convenience init?<Input>(Predicate<Input>)](./init%28_%29.md)
  Creates a predicate by converting an existing predicate.
- [init(value: Bool)](./init%28value%29.md)
  Creates and returns a predicate that always evaluates to a specified Boolean value.
- [init(block: (Any?, [String : Any]?) -> Bool)](./init%28block%29.md)
  Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [init?(fromMetadataQueryString: String)](./init%28frommetadataquerystring%29.md)
  Creates a predicate with a metadata query string.
- [+ predicateWithFormat:](./predicatewithformat_.md)
  Creates and returns a new predicate formed by creating a new string with a specified format and parsing the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/withsubstitutionvariables(_:))*