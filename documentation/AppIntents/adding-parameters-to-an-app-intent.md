# Adding parameters to an app intent

**Framework**: App Intents

Enable people to configure app intents with their custom input values.

#### Overview

Many of your app’s actions likely require input data to perform their work. To help people provide the input that an [`AppIntent`](appintent.md) needs to perform its functionality, add parameters to the intent to tell the system about that data and whether it’s required or optional. When you expose these parameters, people can configure your intents with values unique to their requirements and enable the App Intents framework to mediate with system experiences to write those values at runtime.

For example, the [`Accelerating app interactions with App Intents`](acceleratingappinteractionswithappintents.md) sample code project’s `GetTrailInfo` intent lets people choose which hiking trail information to view when they invoke the app intent. It declares a `trail` parameter by decorating the `trail` property with the [`IntentParameter`](intentparameter.md) property wrapper and provides a title and a description to identify the parameter in the Shortcuts app.

```swift
@Parameter(title: "Trail", description: "The trail to get information on.")
var trail: TrailEntity
```

Note that the example doesn’t provide localized text for the `title` and `description` fields to keep the example focused and make it easy to understand. Always provide localized strings for app intents, App Shortcuts, and their parameters.

##### Make a Parameter Optional or Required

How you define your parameter variables determines whether the system treats that parameter as required or optional. If you define a variable as a non-optional type, the system knows the parameter is required and, when necessary, requests a value. Conversely, if you define a variable as an optional type, the system assumes the parameter is optional and doesn’t request a value. In this scenario, pause the intent and request a value when the intent can’t otherwise proceed by throwing the property wrapper’s [`needsValueError(_:)`](intentparameter/needsvalueerror(_:).md).

```swift
guard let date = date else {
    throw $date.needsValueError("What date would you like to use?")
}
```

##### Define Parameters Using Only the Supported Types

For every parameter you add to your app intent, choose only types that the App Intents framework supports. The system needs to know how to handle your chosen types because it customizes interactions based on those types. The following table lists the supported types.

| Category | Types | Notes |
| --- | --- | --- |
| Primitive value types | [`Bool`](https://developer.apple.com/documentation/Swift/Bool), [`Int`](https://developer.apple.com/documentation/Swift/Int), [`Double`](https://developer.apple.com/documentation/Swift/Double), [`String`](https://developer.apple.com/documentation/Swift/String), [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString), [`Duration`](https://developer.apple.com/documentation/Swift/Duration), [`Date`](https://developer.apple.com/documentation/Foundation/Date), [`Decimal`](https://developer.apple.com/documentation/Foundation/Decimal), [`Measurement`](https://developer.apple.com/documentation/Foundation/Measurement), and [`URL`](https://developer.apple.com/documentation/Foundation/URL) | None |
| Collection types | [`Array`](https://developer.apple.com/documentation/Swift/Array), [`Set`](https://developer.apple.com/documentation/Swift/Set) | Make sure the collection’s elements are of a type that’s compatible with [`IntentParameter`](intentparameter.md). |
| App Intents framework types | [`EntityCollection`](entitycollection.md), [`IntentPerson`](intentperson.md), [`IntentFile`](intentfile.md), [`IntentCurrencyAmount`](intentcurrencyamount.md), [`IntentPaymentMethod`](intentpaymentmethod.md), [`SystemShortcut`](systemshortcut.md), [`UnionValue()`](unionvalue().md) | For additional information, see [`Common data types`](common-data-types.md). |
| Other system types | [`AudioSearch`](https://developer.apple.com/documentation/MediaIntents/AudioSearch), [`DateComponents`](https://developer.apple.com/documentation/Foundation/DateComponents), [`LinkMetadata`](https://developer.apple.com/documentation/LinkPresentation/LinkMetadata), [`PersonNameComponents`](https://developer.apple.com/documentation/Foundation/PersonNameComponents), [`PHAsset`](https://developer.apple.com/documentation/Photos/PHAsset), [`PlaceDescriptor`](https://developer.apple.com/documentation/GeoToolbox/PlaceDescriptor), [`Calendar.RecurrenceRule`](https://developer.apple.com/documentation/Foundation/Calendar/RecurrenceRule), [`SemanticContentDescriptor`](https://developer.apple.com/documentation/VisualIntelligence/SemanticContentDescriptor) | None |
| Custom app data | [`AppEntity`](appentity.md), [`AppEnum`](appenum.md) | Use these types to store app-specific data. |

> **Note**: App intent results support the same set of types.

When you want to specify app-specific data in a parameter, create an [`AppEntity`](appentity.md) or [`AppEnum`](appenum.md) type and use it to specify your data. Apps make their app entities findable using queries, and the system can use those same queries to resolve parameters that contain entities. Similarly, app enums provide a static set of options from which to choose, making it easier for the system to identify possible values.

##### Transform Input Into Your Intent Parameters Types

When a person provides input that your app intents use, the input doesn’t always match the type that your parameters require. For example, natural spoken language commands from Siri are strings, but your app intent might require an integer or floating-point value. To help you with input of various types, use [`Resolvers`](resolvers.md) to leverage the system’s ability to translate one type to another automatically so your app intent can use the input.

##### Restrict Parameter Values

To make it easy for people to provide your app intents with the right information, restrict parameter values. The system presents known values as a list and prompts the person to select one when it needs to resolve a parameter. To restrict parameter values to a list of known values:

- At compile time, use an enumeration type for the parameter that conforms to the [`AppEnum`](appenum.md) protocol.
- At runtime, specify an options provider as part of the property wrapper’s declaration. An *options provider* is a type you implement that conforms to the [`DynamicOptionsProvider`](dynamicoptionsprovider.md) protocol and provides a set of permitted values at runtime.

For example, the [`Accelerating app interactions with App Intents`](acceleratingappinteractionswithappintents.md) sample code project uses a dynamic options provider to display a sorted list of location parameters in the Shortcuts app.

```swift
struct LocationOptionsProvider: DynamicOptionsProvider {
    
    @Dependency
    private var trailManager: TrailDataManager
    
    func results() async throws -> [String] {
        Logger.intentLogging.debug("Getting locations from LocationOptionsProvider")
        
        // Get a list of locations and return it sorted for display, such as in the Shortcuts app.
        return trailManager.uniqueLocations
                .sorted(using: KeyPathComparator(\.self, comparator: .localizedStandard))
    }
}
```

You can configure a parameter with additional options such as enforcing an inclusive range for number types, or specifying the capitalization style and keyboard mode for string types. For more information, see [`IntentParameter`](intentparameter.md).

##### Provide an Interactive Parameter Summary for Your Intent

A parameter summary is a visual, textual outline of your app intent that the Shortcuts app displays in the shortcut editor. The summary can include placeholders that people interact with to choose the values for the intent’s parameters. Even if your intent doesn’t expose any parameters, providing a summary is an opportunity to present more information about your intent in addition to its title.

To add a parameter summary to your intent, implement the protocol’s [`parameterSummary`](appintent/parametersummary.md) requirement and use the provided [`ParameterSummaryBuilder`](parametersummarybuilder.md) result builder to build the summary. Write the content using localized natural language and, where applicable, substitute words that represent parameters with the key paths to those parameters.

```swift
static var parameterSummary: some ParameterSummary {
        Summary("Get information on \(\.$trail)")
    }
```

The shortcut editor substitutes each key path with the corresponding parameter’s title and enables a person to set the value by tapping it. The editor uses the parameter’s type to determine which input controls to display.

Parameter summaries can include conditional statements such as [`AppIntent.When`](appintent/when.md) and [`AppIntent.Switch`](appintent/switch.md) that let the summary update itself in response to already chosen values.

For example, the [`Accelerating app interactions with App Intents`](acceleratingappinteractionswithappintents.md) sample code project uses [`AppIntent.Switch`](appintent/switch.md) in its `SuggestedTrails` app intent:

```swift
    static var parameterSummary: some ParameterSummary {
        Switch(\.$activity) {
            Case(.biking) {
                When(\.$location, .hasAnyValue) {
                    Summary("Ride a bike within \(\.$searchRadius) of \(\.$location)")
                } otherwise: {
                    When(\.$trailCollection, .hasAnyValue) {
                        Summary("Pick a bike ride from \(\.$trailCollection)")
                    } otherwise: {
                        Summary("Suggest bike rides from \(\.$trailCollection) or near \(\.$location)")
                    }
                }
            }
            DefaultCase() {
                When(\.$location, .hasAnyValue) {
                    Summary("Suggest \(\.$activity) trails within \(\.$searchRadius) of \(\.$location)")
                } otherwise: {
                    When(\.$trailCollection, .hasAnyValue) {
                        Summary("Suggest \(\.$activity) trails from \(\.$trailCollection)")
                    } otherwise: {
                        Summary("Suggest \(\.$activity) trails from \(\.$trailCollection) or near \(\.$location)")
                    }
                }
            }
        }
    }
```

##### Review the Role of App Entities

App entities provide the system with information about your app’s data, or about concepts related to your app’s data. App entities describe your app’s custom data types you use for parameters, and help the system resolve parameters for app intents by letting it inspect relevant types. For example, a photo app that provides app entities for its photos and albums might also provide app entities to represent “the most recent photo” or “the default album.” These specific app entities help resolve intents more quickly and with fewer verbal interactions.

Define app entities for core types and concepts that you want to make available to system experiences, and make sure to include properties for any data values that help people discover the entities using queries. For example, create an entity that describes a photo album and add a property to the entity for the name of the photo album.

For more information about expressing your app’s data as entities, see [`Defining app entities for your custom data types`](defining-app-entities-for-your-custom-data-types.md).

## See Also

- [class IntentParameter](intentparameter.md)
  A property wrapper that indicates the associated property is an input argument of the app intent.
- [class IntentParameterDependency](intentparameterdependency.md)
  A property wrapper that represents an app intent dependency you use to provide dynamic options.
- [struct IntentParameterContext](intentparametercontext.md)
  A type that provides information about an associated parameter during value resolution.
- [enum InputConnectionBehavior](inputconnectionbehavior.md)
  Describes the input behaviors for connecting a parameter to the output of the previous App Intent.
- [protocol DynamicOptionsProvider](dynamicoptionsprovider.md)
  An interface for providing a dynamic list of options for a parameter of your app intent.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/adding-parameters-to-an-app-intent)*