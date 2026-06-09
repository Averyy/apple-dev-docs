# Creating your first app intent

**Framework**: App Intents

Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.

#### Overview

An *app intent* is an action that your app performs, and that you make available to the system and other apps. App intents serve as a bridge between your app’s features and Apple Intelligence to enable system experiences like Siri, widgets, the Shortcuts app, and more. For example, when someone asks Siri to play a song using your app, Siri fulfills the request using an app intent you provide. Similarly, people use the Shortcuts app to assemble workflows from the app intents that various apps make available.

As you build your app, create app intents for features that people might want to use from Siri or other parts of the system. For common features that multiple apps share, the system provides templates to use when defining your app intent. These templates simplify the creation of your code and define a common structure that Apple Intelligence uses when responding to prompts. When a template isn’t available, create the app intent code yourself using the available types of the App Intents framework.

##### Declare Your App Intent Type

An app intent is a structure that implements the [`AppIntent`](appintent.md) protocol, which defines the required behavior for all app intents. You use this structure to provide the basic information about your app intent’s action, and to store the data and code you need to perform the action. You create this structure manually for app intents that are unique to your app. However, if you support app intents from one of the system-defined schemas, you can also use Xcode code completion to generate it for you.

Some actions are common to multiple apps on the system, and the system-defined schemas serve as templates for the app intents you create. For example, multiple apps might support playing audio, sending mail or messages, or managing photos and photo albums. To use Xcode code generation to create your initial type, type the domain you support followed by an underscore character and select an app intent from the list Xcode provides. For example, if you type “photos_” into your source file, Xcode displays code completion options from the photos domain. The following example shows the initial code for a show in app search results app intent from the photos domain:

```swift
@AppIntent(schema: .photos.search)
struct SearchMediaIntent: ShowInAppSearchResultsIntent {
    static var searchScopes: [StringSearchScope] = [.general]
    
    var criteria: StringSearchCriteria
    
    func perform() async throws -> some IntentResult {
    }
}
```

> **Note**: If you already declared your app intent structure manually, add support for a schema by adding the `@AppIntent` property wrapper to your declaration. When you add this property wrapper manually, you’re responsible for adding any properties or methods the schema requires. During compilation, the compiler generates errors for any required schema elements missing from your code. Include this property wrapper only if your app intent supports a schema.

For some app intents, you need to declare your type using one of the other protocols the App Intents framework provides. There are several protocols that conform to [`AppIntent`](appintent.md) and unlock additional abilities. For example, if your app intent needs to open your app and display some data, use the [`OpenIntent`](openintent.md) protocol as your starting point instead. In the code above, the structure adopts the [`ShowInAppSearchResultsIntent`](showinappsearchresultsintent.md) protocol because the app intent’s purpose is to show search results in the app’s interface. Choose the protocol that matches the action you support, and fall back to the [`AppIntent`](appintent.md) protocol as needed.

For a list of specialized protocols you can use to define app intents, see [`App intent types`](app-intent-types.md). For a list of app intent schemas organized by functional domains, see [`App schema domains`](app-schema-domains.md).

##### Add Parameters for Any Data You Require

An app intent performs an action, and its parameters specify what data to use when performing the action. Parameters are properties with app-specfic data or settings your app intent code needs to run, and you use them to make your app intent more flexible. For example, instead of creating one app intent type to play songs and another to play albums, you can create one app intent type to play any music your app supports. The parameters of the app intent tell it whether to play a song, an album, or some other type of audio content.

If your app intent supports one of the system-defined schemas, the schema defines which properties are parameters. For app intents you create yourself, you designate properties as parameters by adding the `@Parameter` property wrapper to your declaration. This property wrapper is a typealias for the [`IntentParameter`](intentparameter.md) type, so you can use it to specify additional parameter-related information such as a custom title, description, or Spotlight indexing key. The following example shows a parameter declaration with an optional [`Measurement`](https://developer.apple.com/documentation/Foundation/Measurement) type. The property wrapper parameters tell the system that the property contains a distance in kilometers and that it only supports positive numbers.

```swift
@Parameter(defaultUnit: .kilometers, supportsNegativeNumbers: false)
var searchRadius: Measurement<UnitLength>?
```

> **Note**: The `@Parameter` property wrapper is necessary only for custom app intent types. The app intents you create from system schemas don’t include this wrapper because the system adds it implicitly at compile time and defines relevant values for any attributes.

Before asking an app intent to perform its action, the system resolves all required parameters by filling them with valid data. The system fills in parameter values automatically when it’s able to determine the value reliably. When the value is ambiguous or unavailable, the system can ask the person to supply a prompt using custom UI you provide or using other means. For example, if someone doesn’t specify which song to play, Siri can ask them to say the name of the song. If the system can’t resolve all required parameters, it reports an error.

For more information about adding parameters to your app intent, including the supported types you can use, see [`Adding parameters to an app intent`](adding-parameters-to-an-app-intent.md).

##### Write Code for the Action

An app intent’s main purpose is to perform its designated action, which you do in the [`perform()`](appintent/perform().md) method of your type. Use this method to run your app’s code with the provided parameter data and return a result. The system calls the method only after resolving all required parameters, so your code can rely on the values being present. The following example shows an implementation of this method that navigates to the destination in the `navigationOption` parameter using the same `navigator` object the rest of the app uses for this purpose.

```swift
    func perform() async throws -> some IntentResult {
        await navigator.navigate(to: navigationOption)

        return .result()
    }
```

The system can call your [`perform()`](appintent/perform().md) method under a variety of conditions, so write your code to be as robust as possible. The type of your intent and its configuration determine whether your method runs while your app is in the foreground or background. You can also place your app intent types in an app extension, and run them in a separate process from the rest of your app. Design your code with these possibilities in mind and configure your type to support the capabilities you need:

- **Configure the foreground and background options for your app intent.** Tell the system when to run your app intent in the foreground or background using the [`supportedModes`](appintent/supportedmodes.md) property. Design app intents to run in the background whenever possible, but add foreground modes to faciltate interactions or update your app’s interface.
- **Add support for long-running actions.** If your code needs extra time to run, add support for the [`LongRunningIntent`](longrunningintent.md) protocol to your app intent. This protocol gives you extra time to perform long-running computations or to ensure a critical task such as writing a file to disk is able to finish.
- **Respond gracefully to cancellation requests.** Support system- or person-initiated requests to cancel an in-progress action using the [`CancellableIntent`](cancellableintent.md) protocol. Typically, you combine this protocol with [`LongRunningIntent`](longrunningintent.md) to give people a way to cancel long-running operations safely.
- **Support undoable actions.** If an action affects your app’s interface or content in a way people might want to reverse, add support for the [`UndoableIntent`](undoableintent.md) protocol. This protocol provides an [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) type you can use to add your action to your app’s undo stack.

##### Return a Result Back to the Caller

At the end of your app intent’s [`perform()`](appintent/perform().md) method, you need to return a result back to the system. Results indicate the success or failure of the action, but you can also use them to deliver relevant information back to the system. The following example returns a custom view with information about the selected trail as part of the result. If the system is able to display this view, it can do so to present the result. However, if it isn’t available to display the view, perhaps because the person is using Siri while in their car, it can display or speak the dialog information instead.

```swift
    func perform() async throws -> some IntentResult & ReturnsValue<TrailEntity> & ProvidesDialog & ShowsSnippetView {
        guard let trailData = trailManager.trail(with: trail.id) else {
            throw TrailIntentError.trailNotFound
        }
                
        /**
         You provide a custom view by conforming the return type of the `perform()` function to the `ShowsSnippetView` protocol.
         */
        let snippet = TrailInfoView(trail: trailData, includeConditions: true)
        
        /**
         This intent displays a custom view that includes the trail conditions as part of the view. The dialog includes the trail conditions when
         the system can only read the response, but not display it. When the system can display the response, the dialog omits the trail
         conditions.
         */
        let dialog = IntentDialog(full: "The latest reported conditions for \(trail.name) indicate: \(trail.currentConditions).",
                                  supporting: "Here's the latest information on trail conditions.")
        
        return .result(value: trail, dialog: dialog, view: snippet)
    }
```

The result of an app intent can take many forms:

- An [`IntentDialog`](intentdialog.md) with the text to speak or display.
- The [`ReturnsValue`](returnsvalue.md) or [`ResultsCollection`](resultscollection.md) types, which the system can use as input to another action.
- A [`ShowsSnippetView`](showssnippetview.md) type with a custom view the system can incorporate into response-related interfaces.
- An [`OpensIntent`](opensintent.md) value to direct the system to open your app and display a specific value.

For an example of how to design custom responses, see [`Design custom responses`](acceleratingappinteractionswithappintents#Design-custom-responses.md).

##### Register Dependencies to Other Parts of Your Code

Most app intents are lightweight wrappers that call your app’s existing code to perform their actions. To ensure an app intent has the code it needs to function, you can add dependencies to other types in your app. A dependency tells the system that it can’t run the app intent until the specified object is available. For example, if an app intent requires access to your app’s database, you can create a dependency between the app intent and the object you use to access that database. Configure a dependency by doing the following in your code:

- Register the object on which your app intent depends with the [`AppDependencyManager`](appdependencymanager.md) type.
- Wrap a property in your app intent with the `@Dependency` property wrapper, and store the dependent object in that property.

The system can run app intents soon after your app or app extension launches, so register dependent objects as soon as possible in your app’s code. The following example shows a portion of the initialization code for an app that manages trail information. After creating the trail data manager, the app uses the [`AppDependencyManager`](appdependencymanager.md) type to register the two objects it uses later in an app intent.

```swift
struct AppIntentsSampleApp: App {
    
    private var trailManager: TrailDataManager
    
    init() {
        let trailDataManager = TrailDataManager.shared
        trailManager = trailDataManager

        let navigationModel = NavigationModel(selectedCollection: trailDataManager.nearMeCollection)
        sceneNavigationModel = navigationModel
                
        // Register the trail data manager as a dependent object.
        AppDependencyManager.shared.add(dependency: trailDataManager)
        AppDependencyManager.shared.add(dependency: navigationModel)

        // Additional app initialization...
    }

    // Additional content.
}
```

To access a dependent object, add a property to your app intent and set the property’s name to the variable name you used at registration time. Add the `@Dependency` property wrapper to tell the system to populate the property with the registered object. When creating your app intent, the system automatically populates this property with the dependent object if it’s available. The following example shows an app intent for opening a person’s favorite trails. The code in the intent’s [`perform()`](appintent/perform().md) method uses two previoiusly registered objects to retrieve the favorite trails and show them in the app’s interface.

```swift
struct OpenFavorites: AppIntent {
    
    // Configure any dependent objects on which the app intent relies.
     @Dependency
    private var navigationModel: NavigationModel
    
    @Dependency
    private var trailManager: TrailDataManager

   @MainActor
    func perform() async throws -> some IntentResult {
        navigationModel.selectedCollection = trailManager.favoritesCollection
        
        /// Return an empty result, indicating that the intent is complete.
        return .result()
    }
    
}
```

##### Customize Your App Intents Description and Behavior

Several properties of the [`AppIntent`](appintent.md) protocol provide the system with information about your app intent instance. Implement these properties and use them to describe the action your app intent performs and provide additional configuration details. For each app intent, implement the following properties:

- **[`title`](appintent/title.md)**: Add a short, human-readable description of your app intent’s action.
- **[`description`](appintent/description.md)**: Provide a detailed description of your app intent’s action.
- **[`isDiscoverable`](appintent/isdiscoverable.md)**: Specify whether your app intent is available to the system or private to your app.
- **[`parameterSummary`](appintent/parametersummary.md)**: Provide one or more descriptions of the actions for the Shortcuts app to present to people. Create the descriptions using a [`ParameterSummaryBuilder`](parametersummarybuilder.md) result builder.

For more information about how to create a parameter summary, see [`Adding parameters to an app intent`](adding-parameters-to-an-app-intent.md).

##### Test the Behavior of Your Code in Simulator or on Device

During development, validate that your intents behave as you expect by testing them in Simulator or on-device. If you’re adding intents to a macOS app, build and run the app. For other platforms, select the relevant simulator or connected device and then build and run. After your app launches, follow these steps:

1. Launch the Shortcuts app.
2. Tap or click the New Shortcut (+) button to create a shortcut.
3. Choose Apps in the Action Library’s segmented control.
4. Tap or click your app’s icon.
5. Select the action to test.
6. For app intents with parameters, use the summary to set the parameter values.
7. Tap or click the Run button.

Set a breakpoint at the top of your `perform()` method to confirm your implementation is working. The debugger pauses execution immediately after you run the shortcut, enabling you to step through the code and inspect the intent’s parameters to verify they have the values they require.

Another way to test your code is using the App Intents Testing framework. For more information about how to use it, see [`App Intents Testing`](https://developer.apple.com/documentation/AppIntentsTesting).

## See Also

- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md)
  Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
- [Soup Chef with App Intents: Migrating custom intents](../SiriKit/soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [protocol AppIntent](appintent.md)
  An interface you use to express app-specific actions and make them available to the rest of the system.
- [App intent types](app-intent-types.md)
  Build your intents from types that define common behaviors such as opening or deleting items, playing or recording media, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/creating-your-first-app-intent)*