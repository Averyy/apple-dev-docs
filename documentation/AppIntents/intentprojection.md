# IntentProjection

**Framework**: App Intents  
**Kind**: class

Projections for an app intent that returns non-optional values for parameters.

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
@dynamicMemberLookup
final class IntentProjection<Intent> where Intent : AppIntent
```

#### Overview

Use an `IntentProjection` to create an app intent that returns non-optional values for parameters you list using an [`IntentParameterDependency`](intentparameterdependency.md) property wrapper.

## Topics

### Subscripts
- [subscript<Value>(dynamicMember _: KeyPath<Intent, Value>) -> Value.UnwrappedType](intentprojection/subscript(dynamicmember:).md)

## See Also

- [protocol AppIntentsPackage](appintentspackage.md)
  A type that describes app intent definitions that aren’t part of an app bundle and their dependencies.
- [struct IntentDescription](intentdescription.md)
  The human-readable description and metadata for an app intent.
- [struct IntentDialog](intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [struct IntentDeprecation](intentdeprecation.md)
- [struct IntentSystemContext](intentsystemcontext.md)
  Information that the system makes available to an app intent while it performs its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentprojection)*