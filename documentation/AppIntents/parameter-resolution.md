# Parameter resolution

**Framework**: App Intents

Define the required parameters for your app intents and specify how to resolve those parameters at runtime.

#### Overview

Parameters represent input arguments to your app intents and offer additional metadata to the system. When you define an app intent, add the `@Parameter` property wrapper to any properties you use as input. For example, an app intent that sends a message might include a parameter for the recipient and message string. The system collects and resolves the relevant parameter information before it performs your app intent.

The following partial example shows how to declare parameters for a custom app intent that enables someone to order soup from your app. Configure the parameter property wrapper with any additional details that help the system infer extra information about your parameter.

```swift
struct OrderSoupIntent: AppIntent {
    @Parameter(title: "Soup")
    var soup: Soup
    
    @Parameter(title: "Quantity", inclusiveRange: (1, 10))
    var quantity: Int

    // Other properties
}
```

## Topics

### Intent parameters
- [class IntentParameter](intentparameter.md)
  A property wrapper that indicates the associated property is an input argument of the app intent.
- [class IntentParameterDependency](intentparameterdependency.md)
  A property wrapper that represents an app intent dependency you use to provide dynamic options.
- [struct IntentParameterContext](intentparametercontext.md)
  A type that provides information about an associated parameter during value resolution.
- [enum InputConnectionBehavior](inputconnectionbehavior.md)
  Describes the input behaviors for connecting a parameter to the output of the previous App Intent.
### Parameter choices
- [protocol DynamicOptionsProvider](dynamicoptionsprovider.md)
  An interface for providing a dynamic list of options for a parameter of your app intent.
- [protocol AppEnum](appenum.md)
  An interface to express that a custom type has a predefined, static set of valid values to display.
### Shortcuts support
- [protocol ParameterSummary](parametersummary.md)
  An interface for defining the visual representation of an app intent’s parameters.
- [struct IntentParameterSummary](intentparametersummary.md)
  A type that describes the user interface configuration of an app intent’s parameters.
- [struct ParameterSummaryString](parametersummarystring.md)
  A human-readable string that interpolates parameter key paths to provide user-configurable placeholders in the Shortcuts app.
- [struct ParameterSummaryWhenCondition](parametersummarywhencondition.md)
  A type that represents a conditional statement in a parameter summary.
- [struct ParameterSummarySwitchCondition](parametersummaryswitchcondition.md)
  A type that represents a switch statement in a parameter summary.
- [struct ParameterSummaryCaseCondition](parametersummarycasecondition.md)
  A type that represents an individual case of a switch statement in a parameter summary.
- [struct ParameterSummaryDefaultCaseCondition](parametersummarydefaultcasecondition.md)
  A type that represents the default case of a switch statement in a parameter summary.

## See Also

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [App entities](app-entities.md)
  Make core types or concepts discoverable to the system by declaring them as app entities.
- [Entity queries](entity-queries.md)
  Help the system find the entities your app defines and use them to resolve parameters.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parameter-resolution)*