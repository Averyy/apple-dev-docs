# init(block:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (NSPredicate *) predicateWithBlock:(BOOL (^)(id evaluatedObject, NSDictionary<NSString *,id> *bindings)) block;
```

#### Return Value

A new predicate by that evaluates objects using `block`.

#### Discussion

In macOS 10.6 and later, Core Data supports block-based predicates in the in-memory and atomic stores, but not in the SQLite-based store.

## Parameters

- `block`: The block is applied to the object to be evaluated.

  The block takes two arguments:

  - **evaluatedObject**: The object to be evaluated.
  - **bindings**: The substitution variables dictionary. The dictionary must contain key-value pairs for all variables in the receiver.

  The block returns [`true`](../../Swift/true.md) if the `evaluatedObject` evaluates to true, otherwise [`false`](../../Swift/false.md).

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
- [init?(fromMetadataQueryString: String)](./init%28frommetadataquerystring%29.md)
  Creates a predicate with a metadata query string.
- [+ predicateWithFormat:](./predicatewithformat_.md)
  Creates and returns a new predicate formed by creating a new string with a specified format and parsing the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/init(block:))*