# IntentProjection

**Framework**: App Intents  
**Kind**: class

Projections for an app intent that returns non-optional values for parameters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@dynamicMemberLookup
final class IntentProjection<Intent> where Intent : AppIntent
```

#### Overview

Use an `IntentProjection` to create an app intent that returns non-optional values for parameters you list using an [`IntentParameterDependency`](intentparameterdependency.md) property wrapper.

## Topics

### Subscripts
- [subscript<Value>(dynamicMember _: KeyPath<Intent, Value>) -> Value.UnwrappedType](intentprojection/subscript(dynamicmember:).md)

## See Also

- [protocol DynamicOptionsProvider](dynamicoptionsprovider.md)
  An interface for providing a dynamic list of options for a parameter of your app intent.
- [protocol AppEnum](appenum.md)
  An interface to express that a custom type has a predefined, static set of valid values to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprojection)*