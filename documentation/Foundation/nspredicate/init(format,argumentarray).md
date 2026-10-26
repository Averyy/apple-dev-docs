# init(format:argumentArray:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a predicate by substituting the values in a specified array into a format string and parsing the result.

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
init(format predicateFormat: String, argumentArray arguments: [Any]?)
```

```objc
+ (NSPredicate *) predicateWithFormat:(NSString *) predicateFormat argumentArray:(NSArray *) arguments;
```

#### Return Value

A new predicate by substituting the values in `arguments` into `predicateFormat`, and parsing the result.

#### Discussion

For details of the format of the format string and of limitations on variable substitution, see [Predicate Format String Syntax](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html#//apple_ref/doc/uid/TP40001795).

## Parameters

- `predicateFormat`: The format string for the new predicate.
- `arguments`: The arguments to substitute into `predicateFormat`. Values are substituted in the order they appear in the array.

## See Also

### Creating a Predicate
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
- [init?(fromMetadataQueryString: String)](./init%28frommetadataquerystring%29.md)
  Creates a predicate with a metadata query string.
- [+ predicateWithFormat:](./predicatewithformat_.md)
  Creates and returns a new predicate formed by creating a new string with a specified format and parsing the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/init(format:argumentarray:))*