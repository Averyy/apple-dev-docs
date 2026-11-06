# App Intents Testing

**Framework**: App Intents Testing  
**Kind**: module  
**Role**: Framework

Test your app intents, entities, queries, and integration with system features like Siri or Spotlight.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Overview

The [App Intents](../AppIntents/AppIntents.md) framework allows you to integrate your app with system features like Siri, Shortcuts, or Spotlight. Use App Intents Testing to run and test your app intents, entities, enums, and query logic out-of-process — the same way Siri or Shortcuts perform them. Additionally, with App Intents Testing you can create tests that verify your app’s integration with system features like Siri or Spotlight. The framework provides type-erased APIs that let you reference intents by name, set their parameters, and run them without linking against your app target.

## Topics

### Essentials
- [Testing your App Intents code](./testing-your-app-intents-code.md)
  Evaluate intents, entities, and queries, and verify your integration with system features like Spotlight and Siri.
### Intents, entities, enums, and queries
- [struct IntentDefinitions](./intentdefinitions.md)
  A collection of definitions that catalog your app’s intents, enums, entities, and queries.
### Intent and query result verification
- [struct ResolvedIntentResult](./resolvedintentresult.md)
  A type-safe result from performing an app intent.
- [struct ResolvedValueQueryResult](./resolvedvaluequeryresult.md)
  The result of an intent value query.
### Entity annotation testing
- [struct ViewAnnotation](./viewannotation.md)
  The onscreen context you provide to the system by annotating a view with an app entity.
### Intermediate types
- [struct AnyAppIntent](./anyappintent.md)
  A type-erased, intermediate representation of an app intent for testing purposes.
- [struct AnyAppEntity](./anyappentity.md)
  A type-erased, intermediate representation of your app entity for testing purposes.
- [struct AnyEntityQuery](./anyentityquery.md)
  A type-erased, intermediate representation of your entity query for testing purposes.
- [struct AnyAppEnum](./anyappenum.md)
  A type-erased representation of an app enumeration that provides dynamic enumeration value access.
- [struct AnyTransientAppEntity](./anytransientappentity.md)
  A type-erased representation of a transient app entity that provides dynamic property access.
### Supporting types
- [protocol AppIntentTypeDefinition](./appintenttypedefinition.md)
  A protocol that associates a definition type with its corresponding instance type.
- [struct DynamicPropertyPath](./dynamicpropertypath.md)
  A type-safe, dynamic path to access nested intent values.
- [struct DynamicPropertyPathCollection](./dynamicpropertypathcollection.md)
  Indexed result items from an intent value query.
- [struct IntentValuePropertiesCallable](./intentvaluepropertiescallable.md)
  A callable wrapper that creates app intent instances from keyword arguments.
### Protocols
- [protocol AppEntityExpectationProviding](./appentityexpectationproviding.md)
  A value expectation that checks an app entity’s type and, optionally, its identifier or property values.
- [protocol AppIntentExpectationProviding](./appintentexpectationproviding.md)
  A type that describes the app intent you expect, including its type and, optionally, its parameter values and result.
- [protocol IntentValueExpectation](./intentvalueexpectation.md)
  A type that describes the value you expect for an intent parameter, an app entity property, or an intent result.
- [protocol ResolvableAppEntityExpectation](./resolvableappentityexpectation.md)
  An entity expectation that checks an app entity as the caller passed it, before any query runs.
- [protocol ResolvableIntentValueExpectation](./resolvableintentvalueexpectation.md)
  A value expectation that checks a value as the caller passed it, before any query runs.
### Structures
- [struct AppEntityExpectation](./appentityexpectation.md)
  An expectation that checks an app entity’s type, its property values, and, optionally, its instance identifier.
- [struct AppEntityIdentifierExpectation](./appentityidentifierexpectation.md)
  An expectation that checks whether an app entity is a specific instance by comparing its type and identifier.
- [struct AppIntentExpectation](./appintentexpectation.md)
  An expectation that checks an app intent’s parameters and, optionally, the result the intent returns.
- [struct IntentValueExpectationCallable](./intentvalueexpectationcallable.md)
  A value that you call with labeled value expectations to create an expectation on the corresponding parameters or properties.
- [struct PredicateExpectation](./predicateexpectation.md)
  A value expectation that checks a value of any convertible type against a predicate.
- [struct PrimitiveExpectation](./primitiveexpectation.md)
  A value expectation that checks whether a value is present or whether its string content matches.
- [struct SkillDefinition](./skilldefinition.md)
  A definition that identifies one of an app’s skills by the app’s bundle identifier and the skill’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppIntentsTesting)*