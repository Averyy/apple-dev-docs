# PredicateCodableConfiguration

**Framework**: Foundation  
**Kind**: struct

A specification of the expected types and key paths found in an archived predicate.

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
struct PredicateCodableConfiguration
```

#### Overview

Use this configuration when encoding and decoding a predicate to restrict what that predicate can contain.  If a predicate contains data types or keypaths that aren’t allowed by the configuration, the encoding or decoding process throws an error.

```swift
var configuration = PredicateCodableConfiguration.standardConfiguration
configuration.allowType(Message.self, identifier: "MyApp.Message")
configuration.allowType(Person.self, identifier: "MyApp.Person")
configuration.allowKeyPath(\Message.sender, identifier: "MyApp.Message.sender")
configuration.allowKeyPath(\Person.firstName, identifier: "MyApp.Person.firstName")
configuration.allowKeyPath(\Person.lastName, identifier: "MyApp.Person.lastName")

struct MyRequest: Codable {
    let predicate: Predicate<Message>
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(predicate, forKey: .predicate, configuration: configuration)
    }
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        predicate = try container.decode(Predicate<Message>.self, forKey: .predicate, configuration: configuration)
    }
}
```

## Topics

### Creating a configuration
- [init()](predicatecodableconfiguration/init.md)
- [static let standardConfiguration: PredicateCodableConfiguration](predicatecodableconfiguration/standardconfiguration.md)
### Allowing types and key paths
- [func allow(PredicateCodableConfiguration)](predicatecodableconfiguration/allow(_:).md)
- [func allowKeyPathsForPropertiesProvided<T>(by: T.Type, recursive: Bool)](predicatecodableconfiguration/allowkeypathsforpropertiesprovided(by:recursive:).md)
- [func allowPartialType(any Any.Type, identifier: String)](predicatecodableconfiguration/allowpartialtype(_:identifier:).md)
- [func allowType(any Any.Type, identifier: String?)](predicatecodableconfiguration/allowtype(_:identifier:).md)
### Disallowing types and key paths
- [func disallowKeyPathsForPropertiesProvided<T>(by: T.Type, recursive: Bool)](predicatecodableconfiguration/disallowkeypathsforpropertiesprovided(by:recursive:).md)
- [func disallowPartialType(any Any.Type)](predicatecodableconfiguration/disallowpartialtype(_:).md)
- [func disallowType(any Any.Type)](predicatecodableconfiguration/disallowtype(_:).md)
### Instance Methods
- [func allowKeyPath(any AnyKeyPath & Sendable, identifier: String)](predicatecodableconfiguration/allowkeypath(_:identifier:).md)
- [func disallowKeyPath(any AnyKeyPath & Sendable)](predicatecodableconfiguration/disallowkeypath(_:).md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Predicate](predicate.md)
  A logical condition used to test a set of input values for searching or filtering.
- [struct PredicateError](predicateerror.md)
  An error thrown while evaluating a predicate.
- [protocol PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md)
  A type that provides the expected key paths found in an archived predicate.
- [protocol PredicateExpression](predicateexpression.md)
  A component expression that makes up part of a predicate.
- [protocol StandardPredicateExpression](standardpredicateexpression.md)
  A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [enum PredicateExpressions](predicateexpressions.md)
  The expressions that make up a predicate.
- [struct PredicateBindings](predicatebindings.md)
  A mapping from a predicates’s input variables to their values.
- [class NSPredicate](nspredicate.md)
  A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [class NSExpression](nsexpression.md)
  An expression for use in a comparison predicate.
- [class NSComparisonPredicate](nscomparisonpredicate.md)
  A specialized predicate for comparing expressions.
- [class NSCompoundPredicate](nscompoundpredicate.md)
  A specialized predicate that evaluates logical combinations of other predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicatecodableconfiguration)*