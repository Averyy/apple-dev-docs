# AppIntent Implementations

**Framework**: App Intents

## Topics

### Instance Properties
- [var systemContext: IntentSystemContext](openurlintent/systemcontext.md)
  Context information that’s available while the system performs the app intent’s action.
### Instance Methods
- [func callAsFunction(donate: Bool) async throws](openurlintent/callasfunction(donate:)-6emik.md)
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](openurlintent/callasfunction(donate:)-74ri4.md)
- [func continueInForeground(IntentDialog?, alwaysConfirm: Bool) async throws](openurlintent/continueinforeground(_:alwaysconfirm:).md)
  A method you call to ask a person to continue an action in the foreground.
- [func donate() -> IntentDonationIdentifier](openurlintent/donate-981xn.md)
  Donates the intent to the transcript.
- [func donate() async throws -> IntentDonationIdentifier](openurlintent/donate-d5p6.md)
  Donates the intent to the transcript.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](openurlintent/donate(result:)-89co.md)
  Donates the intent and optional result to the transcript.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](openurlintent/donate(result:)-pm6e.md)
  Donates the intent and optional result to the transcript.
- [func needsToContinueInForegroundError(IntentDialog?, alwaysConfirm: Bool) -> AppIntentError](openurlintent/needstocontinueinforegrounderror(_:alwaysconfirm:).md)
  A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.
- [func requestChoice(between: [IntentChoiceOption], dialog: IntentDialog?) async throws -> IntentChoiceOption](openurlintent/requestchoice(between:dialog:).md)
  Pauses the app intent to request a person to choose from several options.
- [func requestConfirmation() async throws](openurlintent/requestconfirmation.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](openurlintent/requestconfirmation(conditions:actionname:dialog:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws -> Snippet.PerformResult.Value](openurlintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-1owsa.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws](openurlintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-2f7oq.md)
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](openurlintent/requestconfirmation(output:confirmationactionname:showprompt:).md)
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](openurlintent/requestconfirmation(result:confirmationactionname:showprompt:).md)
  Requests user confirmation before performing the app intent.
### Type Aliases
- [OpenURLIntent.Case](openurlintent/case.md)
- [OpenURLIntent.DefaultCase](openurlintent/defaultcase.md)
- [OpenURLIntent.Option](openurlintent/option.md)
  A convenience type alias that represents a choice option within the scope of an app intent.
- [OpenURLIntent.Parameter](openurlintent/parameter.md)
- [OpenURLIntent.Summary](openurlintent/summary.md)
- [OpenURLIntent.Switch](openurlintent/switch.md)
- [OpenURLIntent.When](openurlintent/when.md)
### Type Properties
- [static var authenticationPolicy: IntentAuthenticationPolicy](openurlintent/authenticationpolicy.md)
  A property that defines the authentication policy that indicates whether this app intent requires the device to be unlocked or otherwise authenticated.
- [static var description: IntentDescription?](openurlintent/description.md)
  A description of the app intent that the system shows to people.
- [static var isDiscoverable: Bool](openurlintent/isdiscoverable.md)
  A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.
- [static var openAppWhenRun: Bool](openurlintent/openappwhenrun.md)
  A boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [static var parameterSummary: some ParameterSummary](openurlintent/parametersummary.md)
- [static var supportedModes: IntentModes](openurlintent/supportedmodes.md)
  Defines the supported modes that describe the behavior of your app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/appintent-implementations)*