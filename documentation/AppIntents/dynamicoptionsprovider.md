# DynamicOptionsProvider

**Framework**: App Intents  
**Kind**: protocol

An interface for providing a dynamic list of options for a parameter of your app intent.

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
protocol DynamicOptionsProvider : _SupportsAppDependencies
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)

#### Overview

Implement this protocol in a type that provides a set of possible values for an intent parameter. When configuring the parameter, specify your custom type as the options provider for that parameter. The type of result you return determines how the system displays the information.

- Return an array of [`DisplayRepresentable`](displayrepresentable.md) types to display a list of values.
- Return an array of [`IntentItem`](intentitem.md) types to divide values into sections or configure other presentation options.

The following example shows the configuration of a custom parameter that contains the author name of a book. The options provider offers two possible suggestions for the author name. For brevity, it omits the rest of the implementation.

```swift
struct CreateBook: AppIntent {
    @Parameter(title: "Author Name",
               optionsProvider: AuthorNamesOptionsProvider())
    var authorName: String

    // Other properties and the perform() implementation.

    private struct AuthorNamesOptionsProvider: DynamicOptionsProvider {
        func results() async throws -> [String] {
            ["Juan Chavez", "Anne Johnson"]
        }
    }
}
```

## Topics

### Returning the parameter options
- [func results() async throws -> Self.Result](dynamicoptionsprovider/results.md)
- [func defaultResult() async -> Self.DefaultValue?](dynamicoptionsprovider/defaultresult.md)
  The default value for parameters using this provider when no value is provided by the user.
- [associatedtype Result : ResultsCollection](dynamicoptionsprovider/result.md)
### Associated Types
- [associatedtype DefaultValue : _IntentValue = Self.Result.Result](dynamicoptionsprovider/defaultvalue.md)
### Type Aliases
- [DynamicOptionsProvider.Item](dynamicoptionsprovider/item.md)
- [DynamicOptionsProvider.ItemCollection](dynamicoptionsprovider/itemcollection.md)
- [DynamicOptionsProvider.ItemSection](dynamicoptionsprovider/itemsection.md)
- [DynamicOptionsProvider.ParameterDependency](dynamicoptionsprovider/parameterdependency.md)

## Relationships

### Inherited By
- [EntityPropertyQuery](entitypropertyquery.md)
- [EntityQuery](entityquery.md)
- [EntityStringQuery](entitystringquery.md)
- [EnumerableEntityQuery](enumerableentityquery.md)
- [IndexedEntityQuery](indexedentityquery.md)
- [UniqueAppEntityQuery](uniqueappentityquery.md)
### Conforming Types
- [UniqueAppEntityProvider](uniqueappentityprovider.md)

## See Also

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [class IntentParameter](intentparameter.md)
  A property wrapper that indicates the associated property is an input argument of the app intent.
- [class IntentParameterDependency](intentparameterdependency.md)
  A property wrapper that represents an app intent dependency you use to provide dynamic options.
- [struct IntentParameterContext](intentparametercontext.md)
  A type that provides information about an associated parameter during value resolution.
- [enum InputConnectionBehavior](inputconnectionbehavior.md)
  Describes the input behaviors for connecting a parameter to the output of the previous App Intent.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/dynamicoptionsprovider)*