# AppIntent

**Framework**: App Intents  
**Kind**: protocol

An interface you use to express app-specific actions and make them available to the rest of the system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol AppIntent : PersistentlyIdentifiable, _SupportsAppDependencies, Sendable
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)
- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
- [Displaying static and interactive snippets](displaying-static-and-interactive-snippets.md)
- [Getting started with the App Intents framework](getting-started-with-the-app-intents-framework.md)

#### Overview

The [`AppIntent`](appintent.md) protocol defines the interface you use to make your app’s actions discoverable by Apple Intelligence and Siri, the Shortcuts app, and other system experiences. This protocol defines the common features that help the system identify your app’s actions and access basic information about them. Implement this protocol in all your app intents, and supplement it with other protocols as needed to support specific types of actions.

Implement this protocol in a new type or existing type in your app, app extension, framework, or Swift package. In your type, use the [`perform()`](appintent/perform().md) method to perform the action and return a result back to the system. If you require input from the person performing the action, add one or more variables to your type and apply the `@Parameter` property wrapper to each. For example, an app intent to start a workout might require the person to specify which workout they want. Before calling your [`perform()`](appintent/perform().md) method, the system resolves any parameters with this wrapper by inferring values from the current conversation or by asking someone explicitly to provide the value. If your app intent requires app-specific data to perform its action, apply the `@Dependency` property wrapper to any variables with that data.

In addition to performing an action, an app intent provides information about the action itself. Implement the [`title`](appintent/title.md) and [`description`](appintent/description.md) properties and set them to localized strings describing your action. If your app intent has parameters, fill in the [`parameterSummary`](appintent/parametersummary.md) property with a description of the action and parameters together. The system uses this information during conversations or when displaying information about your intent.

The following example shows an app intent for ordering an album of music. The intent requires the person to specify the album name at order time. The intent also uses an internal album manager type to locate albums by name and initiate the purchase.

```swift
struct OrderAlbum: AppIntent {
    static var title: LocalizedStringResource { "Order Album" }
    static var description = IntentDescription("Order a vinyl record album.")

    @Parameter(title: "Album", description: "The name of the album to order.")
    var albumName: String

   @Dependency
    private var albumManager: AlbumDataManager

    func perform() async throws -> some IntentResult {
        // Perform the action...
        return .result()
    }

    static var parameterSummary: some ParameterSummary {
        Summary("Order \(\.$albumName)")
    }
}
```

In addition to this protocol, you can define intents that support common actions. System-defined schemas define the requirements needed to support common actions, including the app intent protocol your type needs to adopt and any parameters it needs to define. For example, the `AssistantSchemas.PhotosIntent.openAlbum` intent requires conformance to the [`OpenIntent`](openintent.md) protocol and a property with an [`AppEntity`](appentity.md) type for the photo album. For information about the available schemas, see [`App schema domains`](app-schema-domains.md).

For additional app intent protocols you can adopt in your app, see [`App intent types`](app-intent-types.md). For information on how to create an app intent, see [`Creating your first app intent`](creating-your-first-app-intent.md).

## Topics

### Creating an app intent
- [init()](appintent/init.md)
  Creates and returns the app intent.
### Specifying the authentication policy
- [static var authenticationPolicy: IntentAuthenticationPolicy](appintent/authenticationpolicy.md)
  The authentication policy to enforce when running the app intent.
- [enum IntentAuthenticationPolicy](intentauthenticationpolicy.md)
  The authentication policies you can apply to an app intent when it runs.
### Specifying the intent’s allowed target
- [static var allowedExecutionTargets: IntentExecutionTargets](appintent/allowedexecutiontargets.md)
  The list of targets this intent can be executed against.
- [struct IntentExecutionTargets](intentexecutiontargets.md)
  A set of options that describes which process performs an intent or entity query.
- [AppIntent.ExecutionTargets](appintent/executiontargets.md)
### Configuring the metadata
- [static var title: LocalizedStringResource](appintent/title.md)
  A short, localized, human-readable string that conveys the app intent’s action.
- [static var description: IntentDescription?](appintent/description.md)
  A localized string that describes what the app intent does.
- [static var isDiscoverable: Bool](appintent/isdiscoverable.md)
  A Boolean value that indicates whether system features can discover this app intent.
### Performing the action
- [func perform() async throws -> Self.PerformResult](appintent/perform.md)
  Performs the intent’s action and returns a result, after resolving any parameters.
- [var systemContext: IntentSystemContext](appintent/systemcontext.md)
  Contextual information that the system provides while it performs the app intent.
- [associatedtype PerformResult : IntentResult](appintent/performresult.md)
### Running in the foreground or background
- [static var supportedModes: IntentModes](appintent/supportedmodes.md)
  The foreground and background modes the app intent supports.
- [struct IntentModes](intentmodes.md)
  A set of options you use to configure the runtime behavior of an app intent.
- [func continueInForeground(IntentDialog?, alwaysConfirm: Bool) async throws](appintent/continueinforeground(_:alwaysconfirm:).md)
  Attempts to transition the app to the foreground after optionally requesting permission to do so.
- [func needsToContinueInForegroundError(IntentDialog?, alwaysConfirm: Bool) -> AppIntentError](appintent/needstocontinueinforegrounderror(_:alwaysconfirm:).md)
  Asks the person to continue the intent’s action in the foreground.
### Requesting more information
- [func requestChoice(between: [IntentChoiceOption], dialog: IntentDialog?) async throws -> IntentChoiceOption](appintent/requestchoice(between:dialog:).md)
  Pauses the app intent and asks the person to choose an option from the specified list.
- [func requestChoice<Content>(between: [IntentChoiceOption], dialog: IntentDialog?, content: () -> Content) async throws -> IntentChoiceOption](appintent/requestchoice(between:dialog:content:).md)
  Pauses the app intent, asks the person to choose from the specified options, and provides additional content related to those options.
- [func requestChoice<Content>(between: [IntentChoiceOption], dialog: IntentDialog?, view: Content) async throws -> IntentChoiceOption](appintent/requestchoice(between:dialog:view:).md)
  Pauses the app intent, asks the person to choose from the specified options, and provides a view with additional data.
### Requesting confirmation
- [func requestConfirmation() async throws](appintent/requestconfirmation.md)
  Displays a prompt that asks the person for confirmation before performing the app intent.
- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](appintent/requestconfirmation(conditions:actionname:dialog:).md)
  Displays a confirmation prompt that includes the specified text and action details.
- [func requestConfirmation<Content>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, content: () -> Content) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:content:).md)
  Displays a confirmation prompt with an interactive snippet.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-3vewj.md)
  Displays a confirmation prompt that includes an interactive snippet.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws -> Snippet.PerformResult.Value](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-jxb8.md)
  Displays a confirmation prompt with an interactive snippet.
### Donating the intent to the system
- [func donate() async throws -> IntentDonationIdentifier](appintent/donate-1e60c.md)
  Donates the app intent to the system asynchronously.
- [func donate() -> IntentDonationIdentifier](appintent/donate-jp6k.md)
  Donates the app intent to the system.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](appintent/donate(result:)-36cia.md)
  Donates the app intent and a result to the system asynchronously.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](appintent/donate(result:)-9b25i.md)
  Donates the app intent and a result to the system asynchronously.
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](appintent/callasfunction(donate:)-3qvbt.md)
  Runs the intent’s action after resolving any parameters, returns the resulting value, and optionally donates the intent to the system.
- [func callAsFunction(donate: Bool) async throws](appintent/callasfunction(donate:)-7v1om.md)
  Runs the intent’s action after resolving any parameters, and optionally donates the intent to the system.
### Summarizing the parameters
- [associatedtype SummaryContent : ParameterSummary](appintent/summarycontent.md)
  The type of parameter summary representing this intent.
- [static var parameterSummary: Self.SummaryContent](appintent/parametersummary.md)
  The parameter summary the Shortcuts app uses to generate shortcuts for this intent.
- [static var parameterSummary: some ParameterSummary](appintent/parametersummary-4vgic.md)
- [enum ParameterSummaryBuilder](parametersummarybuilder.md)
  A result builder that allows you to declaratively describe a parameter summary.
- [AppIntent.Parameter](appintent/parameter.md)
- [AppIntent.Case](appintent/case.md)
- [AppIntent.DefaultCase](appintent/defaultcase.md)
- [AppIntent.Summary](appintent/summary.md)
- [AppIntent.Switch](appintent/switch.md)
- [AppIntent.When](appintent/when.md)
- [AppIntent.Option](appintent/option.md)
  A convenience type alias that represents a choice option within the scope of an app intent.
### Deprecated
- [static var openAppWhenRun: Bool](appintent/openappwhenrun.md)
  A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(result:confirmationactionname:showprompt:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(output:confirmationactionname:showprompt:).md)

## Relationships

### Inherits From
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [AssistantIntent](assistantintent.md)
- [AssistantSchemaIntent](assistantschemaintent.md)
- [AudioPlaybackIntent](audioplaybackintent.md)
- [AudioRecordingIntent](audiorecordingintent.md)
- [AudioStartingIntent](audiostartingintent.md)
- [CameraCaptureIntent](cameracaptureintent.md)
- [CancellableIntent](cancellableintent.md)
- [ControlConfigurationIntent](controlconfigurationintent.md)
- [CustomIntentMigratedAppIntent](customintentmigratedappintent.md)
- [DeleteIntent](deleteintent.md)
- [DeprecatedAppIntent](deprecatedappintent.md)
- [ForegroundContinuableIntent](foregroundcontinuableintent.md)
- [LiveActivityIntent](liveactivityintent.md)
- [LiveActivityStartingIntent](liveactivitystartingintent.md)
- [LongRunningIntent](longrunningintent.md)
- [OpenIntent](openintent.md)
- [PauseWorkoutIntent](pauseworkoutintent.md)
- [PlayVideoIntent](playvideointent.md)
- [PredictableIntent](predictableintent.md)
- [ProgressReportingIntent](progressreportingintent.md)
- [PushToTalkTransmissionIntent](pushtotalktransmissionintent.md)
- [ResumeWorkoutIntent](resumeworkoutintent.md)
- [SetFocusFilterIntent](setfocusfilterintent.md)
- [SetValueIntent](setvalueintent.md)
- [ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
- [SnippetIntent](snippetintent.md)
- [StartDiveIntent](startdiveintent.md)
- [StartWorkoutIntent](startworkoutintent.md)
- [SystemIntent](systemintent.md)
- [TargetContentProvidingIntent](targetcontentprovidingintent.md)
- [UISceneAppIntent](uisceneappintent.md)
- [URLRepresentableIntent](urlrepresentableintent.md)
- [UndoableIntent](undoableintent.md)
- [WidgetConfigurationIntent](widgetconfigurationintent.md)
### Conforming Types
- [EmptySnippetIntent](emptysnippetintent.md)
- [OpenURLIntent](openurlintent.md)
- [RunSystemShortcutIntent](runsystemshortcutintent.md)

## See Also

- [Creating your first app intent](creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md)
  Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
- [Soup Chef with App Intents: Migrating custom intents](../SiriKit/soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [App intent types](app-intent-types.md)
  Build your intents from types that define common behaviors such as opening or deleting items, playing or recording media, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent)*