# InputConnectionBehavior

**Framework**: App Intents  
**Kind**: enum

Describes the input behaviors for connecting a parameter to the output of the previous App Intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum InputConnectionBehavior
```

## Topics

### Getting the connection behaviors
- [InputConnectionBehavior.default](inputconnectionbehavior/default.md)
  A behavior that allows the system to determine if the parameter accepts the output.
- [InputConnectionBehavior.never](inputconnectionbehavior/never.md)
  A behavior that prohibits the parameter from accepting the output.
- [InputConnectionBehavior.connectToPreviousIntentResult](inputconnectionbehavior/connecttopreviousintentresult.md)
  A behavior that permits the parameter to accept the output.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class IntentParameter](intentparameter.md)
  A property wrapper that indicates the associated property is an input argument of the app intent.
- [class IntentParameterDependency](intentparameterdependency.md)
  A property wrapper that represents an app intent dependency you use to provide dynamic options.
- [struct IntentParameterContext](intentparametercontext.md)
  A type that provides information about an associated parameter during value resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/inputconnectionbehavior)*