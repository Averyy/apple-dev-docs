# PredicateCodableConfiguration

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init()](./predicatecodableconfiguration/init%28%29.md)
- [static let standardConfiguration: PredicateCodableConfiguration](./predicatecodableconfiguration/standardconfiguration.md)
### Allowing types and key paths
- [func allow(PredicateCodableConfiguration)](./predicatecodableconfiguration/allow%28_%29.md)
- [func allowKeyPathsForPropertiesProvided<T>(by: T.Type, recursive: Bool)](./predicatecodableconfiguration/allowkeypathsforpropertiesprovided%28by,recursive%29.md)
- [func allowPartialType(any Any.Type, identifier: String)](./predicatecodableconfiguration/allowpartialtype%28_,identifier%29.md)
- [func allowType(any Any.Type, identifier: String?)](./predicatecodableconfiguration/allowtype%28_,identifier%29.md)
### Disallowing types and key paths
- [func disallowKeyPathsForPropertiesProvided<T>(by: T.Type, recursive: Bool)](./predicatecodableconfiguration/disallowkeypathsforpropertiesprovided%28by,recursive%29.md)
- [func disallowPartialType(any Any.Type)](./predicatecodableconfiguration/disallowpartialtype%28_%29.md)
- [func disallowType(any Any.Type)](./predicatecodableconfiguration/disallowtype%28_%29.md)
### Instance Methods
- [func allowKeyPath(any AnyKeyPath & Sendable, identifier: String)](./predicatecodableconfiguration/allowkeypath%28_,identifier%29.md)
- [func disallowKeyPath(any AnyKeyPath & Sendable)](./predicatecodableconfiguration/disallowkeypath%28_%29.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Filltering
- [struct Predicate](./predicate.md)
  A logical condition used to test a set of input values for searching or filtering.
- [struct PredicateError](./predicateerror.md)
  An error thrown while evaluating a predicate.
- [protocol PredicateCodableKeyPathProviding](./predicatecodablekeypathproviding.md)
  A type that provides the expected key paths found in an archived predicate.
- [protocol PredicateExpression](./predicateexpression.md)
  A component expression that makes up part of a predicate.
- [protocol StandardPredicateExpression](./standardpredicateexpression.md)
  A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [enum PredicateExpressions](./predicateexpressions.md)
  The expressions that make up a predicate.
- [struct PredicateBindings](./predicatebindings.md)
  A mapping from a predicates’s input variables to their values.
- [class NSPredicate](./nspredicate.md)
  A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [class NSExpression](./nsexpression.md)
  An expression for use in a comparison predicate.
- [class NSComparisonPredicate](./nscomparisonpredicate.md)
  A specialized predicate for comparing expressions.
- [class NSCompoundPredicate](./nscompoundpredicate.md)
  A specialized predicate that evaluates logical combinations of other predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicatecodableconfiguration)*