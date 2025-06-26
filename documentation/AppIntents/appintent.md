# AppIntent

**Framework**: App Intents  
**Kind**: protocol

An interface for providing an app-specific capability that people invoke from system experiences like Siri and the Shortcuts app.

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
protocol AppIntent : PersistentlyIdentifiable, _SupportsAppDependencies, Sendable
```

## Mentions

- [Making actions and content discoverable and widely available](making-actions-and-content-discoverable-and-widely-available.md)
- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Creating your first app intent](creating-your-first-app-intent.md)
- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
- [Displaying static and interactive snippets](displaying-static-and-interactive-snippets.md)
- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)

#### Overview

To expose your app’s functionality to system experiences like Siri or the Shortcuts app, and to support interactivity in widgets, you need to implement the `AppIntent` protocol. Use it to provide phrases that can trigger the functionality, describe the needed data for the functionality you make available, and implement the method that performs the functionality.

The system instantiates an app intent you create parameter-less using the [`init()`](appintent/init().md) initializer whenever a person invokes it through a system service like Siri, Shortcuts, and so on. If available, the system sets parameters based on user input or other available sources. With set parameters, the system attempts to resolve them in the order of their declaration in the `AppIntent` body. After it resolves all parameters, the system calls [`perform()`](appintent/perform().md) to perform the app intent with its configured parameters. Note that the system retains the app intent and its output only for the duration of the invocation.

> **Note**:  Session 10032: [`Dive into App Intents`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10032).

##### Implement the Appintent Protocol

Declare a custom intent type by defining a structure that conforms to the `AppIntent` protocol:

```swift
struct OrderSoupIntent: AppIntent {
   static var title = LocalizedStringResource("Order Soup")
   static var description = IntentDescription("Orders a soup from your favorite restaurant.")
}
```

Then, declare the AppIntent’s parameters. When you implement an `AppIntent` type, parameters must be declared with the `@Parameter` property wrapper. For more information about declaring parameters, see [`Adding parameters to an app intent`](adding-parameters-to-an-app-intent.md).

```swift
struct OrderSoupIntent: AppIntent {
   @Parameter(title: "Soup")
   var soup: Soup

   @Parameter(title: "Quantity")
   var quantity: Int?
}
```

Next, implement the required [`perform()`](appintent/perform().md)function: Validate your intent’s parameters, execute the intent, and return an [`IntentResult`](intentresult.md) that represents the output of a completed intent; for example, a [`PerformResult`](appintent/performresult.md).

```swift
struct OrderSoupIntent: AppIntent {
    @Parameter(title: "Soup")
    var soup: Soup

    @Parameter(title: "Quantity")
    var quantity: Int?

    static var parameterSummary: some ParameterSummary {
        Summary("Order \(\.$soup)") {
            \.$quantity
        }
    }

    func perform() async throws -> some IntentResult {
        guard let quantity = quantity, quantity < 10 else {
            throw $quantity.needsValue
        }
        soup.order(quantity: quantity)
        return .result()
    }
}
```

## Topics

### Creating an app intent
- [init()](appintent/init.md)
  Creates an app intent.
### Specifying the authentication policy
- [static var authenticationPolicy: IntentAuthenticationPolicy](appintent/authenticationpolicy.md)
  A property that defines the authentication policy that indicates whether this app intent requires the device to be unlocked or otherwise authenticated.
- [enum IntentAuthenticationPolicy](intentauthenticationpolicy.md)
  An enumeration that describes the authentication policy to use when running an app intent.
### Configuring the metadata
- [static var title: LocalizedStringResource](appintent/title.md)
  A short, localized, human-readable string that describes the app intent using a verb and a noun in title case.
- [static var description: IntentDescription?](appintent/description.md)
  A description of the app intent that the system shows to people.
- [static var openAppWhenRun: Bool](appintent/openappwhenrun.md)
  A boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [static var isDiscoverable: Bool](appintent/isdiscoverable.md)
  A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.
### Performing the action
- [func perform() async throws -> Self.PerformResult](appintent/perform.md)
  Performs the intent after resolving the provided parameters.
- [var systemContext: IntentSystemContext](appintent/systemcontext.md)
  Context information that’s available while the system performs the app intent’s action.
- [associatedtype PerformResult : IntentResult](appintent/performresult.md)
### Requesting confirmation
- [func requestConfirmation() async throws](appintent/requestconfirmation.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](appintent/requestconfirmation(conditions:actionname:dialog:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Content>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, content: () -> Content) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:content:).md)
  Request user confirmation before performing the app intent.
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(result:confirmationactionname:showprompt:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(output:confirmationactionname:showprompt:).md)
### Donating the intent to the system
- [func donate() async throws -> IntentDonationIdentifier](appintent/donate-1e60c.md)
  Donates the intent to the transcript.
- [func donate() -> IntentDonationIdentifier](appintent/donate-jp6k.md)
  Donates the intent to the transcript.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](appintent/donate(result:)-36cia.md)
  Donates the intent and optional result to the transcript.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](appintent/donate(result:)-9b25i.md)
  Donates the intent and optional result to the transcript.
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](appintent/callasfunction(donate:)-3qvbt.md)
- [func callAsFunction(donate: Bool) async throws](appintent/callasfunction(donate:)-7v1om.md)
### Summarizing the parameters
- [associatedtype SummaryContent : ParameterSummary](appintent/summarycontent.md)
  The type of parameter summary representing this intent.
- [static var parameterSummary: Self.SummaryContent](appintent/parametersummary.md)
  Defines the summary of this intent in relation to how its parameters are populated.
- [static var parameterSummary: some ParameterSummary](appintent/parametersummary-4vgic.md)
- [enum ParameterSummaryBuilder](parametersummarybuilder.md)
  A result builder that allows you to declaratively describe a parameter summary.
- [AppIntent.Parameter](appintent/parameter.md)
- [AppIntent.Case](appintent/case.md)
- [AppIntent.DefaultCase](appintent/defaultcase.md)
- [AppIntent.Summary](appintent/summary.md)
- [AppIntent.Switch](appintent/switch.md)
- [AppIntent.When](appintent/when.md)
### Instance Methods
- [func continueInForeground(IntentDialog?, alwaysConfirm: Bool) async throws](appintent/continueinforeground(_:alwaysconfirm:).md)
  A method you call to ask a person to continue an action in the foreground.
- [func needsToContinueInForegroundError(IntentDialog?, alwaysConfirm: Bool) -> AppIntentError](appintent/needstocontinueinforegrounderror(_:alwaysconfirm:).md)
  A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.
- [func requestChoice(between: [IntentChoiceOption], dialog: IntentDialog?) async throws -> IntentChoiceOption](appintent/requestchoice(between:dialog:).md)
  Pauses the app intent to request a person to choose from several options.
- [func requestChoice<Content>(between: [IntentChoiceOption], dialog: IntentDialog?, content: () -> Content) async throws -> IntentChoiceOption](appintent/requestchoice(between:dialog:content:).md)
  Pauses the app intent to request a person to choose from several options.
- [func requestChoice<Content>(between: [IntentChoiceOption], dialog: IntentDialog?, view: Content) async throws -> IntentChoiceOption](appintent/requestchoice(between:dialog:view:).md)
  Pauses the app intent to request a person to choose from several options.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-3vewj.md)
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws -> Snippet.PerformResult.Value](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-jxb8.md)
  Requests user confirmation before performing the app intent.
### Type Aliases
- [AppIntent.Option](appintent/option.md)
  A convenience type alias that represents a choice option within the scope of an app intent.
### Type Properties
- [static var supportedModes: IntentModes](appintent/supportedmodes.md)
  Defines the supported modes that describe the behavior of your app intent.

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
- [ControlConfigurationIntent](controlconfigurationintent.md)
- [CustomIntentMigratedAppIntent](customintentmigratedappintent.md)
- [DeleteIntent](deleteintent.md)
- [DeprecatedAppIntent](deprecatedappintent.md)
- [ForegroundContinuableIntent](foregroundcontinuableintent.md)
- [LiveActivityIntent](liveactivityintent.md)
- [LiveActivityStartingIntent](liveactivitystartingintent.md)
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

## See Also

- [protocol AudioPlaybackIntent](audioplaybackintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol AudioRecordingIntent](audiorecordingintent.md)
  An app intent that starts, stops or otherwise modifies audio recording state.
- [protocol AudioStartingIntent](audiostartingintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol CameraCaptureIntent](cameracaptureintent.md)
  Designates intent that will launch an activity that uses device’s camera to capture photos or videos. Marking your intent with this protocol makes it available as a possible action for Camera quick action.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.
- [protocol ForegroundContinuableIntent](foregroundcontinuableintent.md)
  A protocol you use for app intents which begin their work with the app in the background but may request to continue in the foreground.
- [protocol OpenIntent](openintent.md)
  Open the associated item.
- [struct OpenURLIntent](openurlintent.md)
  An intent that opens a universal link.
- [protocol PlayVideoIntent](playvideointent.md)
  An intent that looks for videos based on a search term, then plays the content.
- [protocol ProgressReportingIntent](progressreportingintent.md)
  An intent that reports progress to the system during its execution
- [protocol PushToTalkTransmissionIntent](pushtotalktransmissionintent.md)
  An intent that begins or ends an audio transmission with the Push to Talk framework.
- [protocol URLRepresentableIntent](urlrepresentableintent.md)
  An app intent with a URL representation.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent)*