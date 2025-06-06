# Resolvers

**Framework**: App Intents

Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.

#### Overview

System experiences like Siri and the Shortcuts app produce input that doesn’t always match what your code requires. For example, natural spoken language commands from Siri are strings, but your app intent might require an integer or floating-point value instead. Resolvers let the system translate one type to another automatically.

The system provides resolvers to convert between integer, floating-point, Boolean, string, and URL types. As needed, the system can chain multiple resolvers together to translate between types for which no single resolver exists. For example, it can translate an integer into a string and then translate the string into a Boolean value. If your app defines custom types, create your own resolvers to translate those types to more recognizable values.

## Topics

### Integer resolution
- [struct IntFromDoubleResolver](intfromdoubleresolver.md)
  A resolver that converts a double into an integer using the specified rounding rule and validates the result is within the parameter’s inclusive range.
- [struct IntFromStringResolver](intfromstringresolver.md)
  A resolver that converts a string into an integer in the specified base and validates the result is within the parameter’s inclusive range.
- [struct IntResolver](intresolver.md)
  A resolver that validates an integer is within the parameter’s inclusive range.
### Floating-point resolution
- [struct DoubleFromIntResolver](doublefromintresolver.md)
- [struct DoubleFromStringResolver](doublefromstringresolver.md)
  A resolver that converts a string into a double and validates the result is within the parameter’s inclusive range.
- [struct DoubleResolver](doubleresolver.md)
  A resolver that validates a double is within the parameter’s inclusive range.
### String resolution
- [struct AttributedStringFromStringResolver](attributedstringfromstringresolver.md)
  A resolver that converts a string into an attributed string.
- [struct StringFromDoubleResolver](stringfromdoubleresolver.md)
  A resolver that converts a double into a string.
- [struct StringFromIntResolver](stringfromintresolver.md)
  A resolver that converts one or more integers into one or more strings.
### Boolean resolution
- [struct BoolFromStringResolver](boolfromstringresolver.md)
  A resolver that converts a string into a Boolean, optionally using a localized display name.
### URL resolution
- [struct URLFromStringResolver](urlfromstringresolver.md)
  A resolver that converts a string into a URL.
### Custom resolution
- [protocol Resolver](resolver.md)
  An interface to convert a value from one type to a different type.
### Range validation
- [protocol RangeCheckingResolver](rangecheckingresolver.md)
  An interface for validating that a value is within a parameter’s defined inclusive range.
- [protocol RangeComparableProperty](rangecomparableproperty.md)

## See Also

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [Parameter resolution](parameter-resolution.md)
  Define the required parameters for your app intents and specify how to resolve those parameters at runtime.
- [App entities](app-entities.md)
  Make core types or concepts discoverable to the system by declaring them as app entities.
- [Entity queries](entity-queries.md)
  Help the system find the entities your app defines and use them to resolve parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolvers)*