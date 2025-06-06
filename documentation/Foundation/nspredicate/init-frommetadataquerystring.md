# init(fromMetadataQueryString:)

**Framework**: Foundation  
**Kind**: init

Creates a predicate with a metadata query string.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init?(fromMetadataQueryString queryString: String)
```

#### Discussion

For details of the format of the query string, see [`File Metadata Query Expression Syntax`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/QueryFormat.html#//apple_ref/doc/uid/TP40001849).

## Parameters

- `queryString`: A metadata query string.

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
- [init(value: Bool)](nspredicate/init(value:).md)
  Creates and returns a predicate that always evaluates to a specified Boolean value.
- [init(block: (Any?, [String : Any]?) -> Bool)](nspredicate/init(block:).md)
  Creates a predicate that evaluates using a specified block object and bindings dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/init(frommetadataquerystring:))*