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

- [struct IntentModes](intentmodes.md)
  A set of options you use to configure the runtime behavior of an app intent.
- [struct IntentSystemContext](intentsystemcontext.md)
  Contextual information that the system provides while it performs an app intent.
- [struct IntentDescription](intentdescription.md)
  The human-readable description and metadata for an app intent.
- [struct IntentDialog](intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [struct IntentDeprecation](intentdeprecation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprojection)*