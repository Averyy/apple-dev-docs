# init(fromMetadataQueryString:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a predicate with a metadata query string.

**Availability**:
- macOS 10.9+

## Declaration

```swift
init?(fromMetadataQueryString queryString: String)
```

```objc
+ (NSPredicate *) predicateFromMetadataQueryString:(NSString *) queryString;
```

#### Discussion

For details of the format of the query string, see [File Metadata Query Expression Syntax](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/QueryFormat.html#//apple_ref/doc/uid/TP40001849).

## Parameters

- `queryString`: A metadata query string.

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
- [func withSubstitutionVariables([String : Any]) -> Self](./withsubstitutionvariables%28_%29.md)
  Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [init(value: Bool)](./init%28value%29.md)
  Creates and returns a predicate that always evaluates to a specified Boolean value.
- [init(block: (Any?, [String : Any]?) -> Bool)](./init%28block%29.md)
  Creates a predicate that evaluates using a specified block object and bindings dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/init(frommetadataquerystring:))*