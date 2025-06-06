# init(block:)

**Framework**: Foundation  
**Kind**: init

Creates a predicate that evaluates using a specified block object and bindings dictionary.

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
init(block: @escaping (Any?, [String : Any]?) -> Bool)
```

#### Return Value

A new predicate by that evaluates objects using `block`.

#### Discussion

In macOS 10.6 and later, Core Data supports block-based predicates in the in-memory and atomic stores, but not in the SQLite-based store.

## Parameters

- `block`: The block returns   if the   evaluates to true, otherwise  .

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
- [init?(fromMetadataQueryString: String)](nspredicate/init(frommetadataquerystring:).md)
  Creates a predicate with a metadata query string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/init(block:))*