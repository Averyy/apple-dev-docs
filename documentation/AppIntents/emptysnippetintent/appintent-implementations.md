# AppIntent Implementations

**Framework**: App Intents

## Topics

### Instance Properties
- [var systemContext: IntentSystemContext](emptysnippetintent/systemcontext.md)
  Context information that’s available while the system performs the app intent’s action.
### Instance Methods
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](emptysnippetintent/callasfunction(donate:)-6n81w.md)
- [func callAsFunction(donate: Bool) async throws](emptysnippetintent/callasfunction(donate:)-7xt20.md)
- [func continueInForeground(IntentDialog?, alwaysConfirm: Bool) async throws](emptysnippetintent/continueinforeground(_:alwaysconfirm:).md)
  A method you call to ask a person to continue an action in the foreground.
- [func donate() -> IntentDonationIdentifier](emptysnippetintent/donate-412wf.md)
  Donates the intent to the transcript.
- [func donate() async throws -> IntentDonationIdentifier](emptysnippetintent/donate-8h49.md)
  Donates the intent to the transcript.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](emptysnippetintent/donate(result:)-20key.md)
  Donates the intent and optional result to the transcript.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](emptysnippetintent/donate(result:)-3gngj.md)
  Donates the intent and optional result to the transcript.
- [func needsToContinueInForegroundError(IntentDialog?, alwaysConfirm: Bool) -> AppIntentError](emptysnippetintent/needstocontinueinforegrounderror(_:alwaysconfirm:).md)
  A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.
- [func requestChoice(between: [IntentChoiceOption], dialog: IntentDialog?) async throws -> IntentChoiceOption](emptysnippetintent/requestchoice(between:dialog:).md)
  Pauses the app intent to request a person to choose from several options.
- [func requestConfirmation() async throws](emptysnippetintent/requestconfirmation.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](emptysnippetintent/requestconfirmation(conditions:actionname:dialog:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws](emptysnippetintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-4ynth.md)
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws -> Snippet.PerformResult.Value](emptysnippetintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-6tx44.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](emptysnippetintent/requestconfirmation(output:confirmationactionname:showprompt:).md)
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](emptysnippetintent/requestconfirmation(result:confirmationactionname:showprompt:).md)
  Requests user confirmation before performing the app intent.
### Type Aliases
- [EmptySnippetIntent.Case](emptysnippetintent/case.md)
- [EmptySnippetIntent.DefaultCase](emptysnippetintent/defaultcase.md)
- [EmptySnippetIntent.Option](emptysnippetintent/option.md)
  A convenience type alias that represents a choice option within the scope of an app intent.
- [EmptySnippetIntent.Parameter](emptysnippetintent/parameter.md)
- [EmptySnippetIntent.Summary](emptysnippetintent/summary.md)
- [EmptySnippetIntent.Switch](emptysnippetintent/switch.md)
- [EmptySnippetIntent.When](emptysnippetintent/when.md)
### Type Properties
- [static var authenticationPolicy: IntentAuthenticationPolicy](emptysnippetintent/authenticationpolicy.md)
  A property that defines the authentication policy that indicates whether this app intent requires the device to be unlocked or otherwise authenticated.
- [static var description: IntentDescription?](emptysnippetintent/description.md)
  A description of the app intent that the system shows to people.
- [static var isDiscoverable: Bool](emptysnippetintent/isdiscoverable-44ooy.md)
  A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.
- [static var openAppWhenRun: Bool](emptysnippetintent/openappwhenrun.md)
  A boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [static var parameterSummary: some ParameterSummary](emptysnippetintent/parametersummary.md)
- [static var supportedModes: IntentModes](emptysnippetintent/supportedmodes.md)
  Defines the supported modes that describe the behavior of your app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/emptysnippetintent/appintent-implementations)*