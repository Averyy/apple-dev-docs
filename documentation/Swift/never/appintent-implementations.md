# AppIntent Implementations

**Framework**: Swift

## Topics

### Initializers
- [init()](never/init.md)
  Creates an app intent.
### Instance Properties
- [var systemContext: IntentSystemContext](never/systemcontext.md)
  Context information that’s available while the system performs the app intent’s action.
### Instance Methods
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](never/callasfunction(donate:)-6myy3.md)
- [func callAsFunction(donate: Bool) async throws](never/callasfunction(donate:)-92w61.md)
- [func continueInForeground(IntentDialog?, alwaysConfirm: Bool) async throws](never/continueinforeground(_:alwaysconfirm:).md)
  A method you call to ask a person to continue an action in the foreground.
- [func donate() -> IntentDonationIdentifier](never/donate-4ylpx.md)
  Donates the intent to the transcript.
- [func donate() async throws -> IntentDonationIdentifier](never/donate-5ypn3.md)
  Donates the intent to the transcript.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](never/donate(result:)-9und8.md)
  Donates the intent and optional result to the transcript.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](never/donate(result:)-rsyn.md)
  Donates the intent and optional result to the transcript.
- [func needsToContinueInForegroundError(IntentDialog?, alwaysConfirm: Bool) -> AppIntentError](never/needstocontinueinforegrounderror(_:alwaysconfirm:).md)
  A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.
- [func perform() async throws -> IntentResultContainer<Never, Never, Never, Never>](never/perform.md)
  Performs the intent after resolving the provided parameters.
- [func requestChoice(between: [IntentChoiceOption], dialog: IntentDialog?) async throws -> IntentChoiceOption](never/requestchoice(between:dialog:).md)
  Pauses the app intent to request a person to choose from several options.
- [func requestConfirmation() async throws](never/requestconfirmation.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](never/requestconfirmation(conditions:actionname:dialog:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws -> Snippet.PerformResult.Value](never/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-2frdj.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws](never/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-888lr.md)
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](never/requestconfirmation(output:confirmationactionname:showprompt:).md)
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](never/requestconfirmation(result:confirmationactionname:showprompt:).md)
  Requests user confirmation before performing the app intent.
### Type Aliases
- [typealias Case](never/case.md)
- [typealias DefaultCase](never/defaultcase.md)
- [typealias Option](never/option.md)
  A convenience type alias that represents a choice option within the scope of an app intent.
- [typealias Parameter](never/parameter.md)
- [typealias PerformResult](never/performresult.md)
- [typealias Summary](never/summary.md)
- [typealias SummaryContent](never/summarycontent.md)
  The type of parameter summary representing this intent.
- [typealias Switch](never/switch.md)
- [typealias When](never/when.md)
### Type Properties
- [static var authenticationPolicy: IntentAuthenticationPolicy](never/authenticationpolicy.md)
  A property that defines the authentication policy that indicates whether this app intent requires the device to be unlocked or otherwise authenticated.
- [static var description: IntentDescription?](never/description.md)
  A description of the app intent that the system shows to people.
- [static var isDiscoverable: Bool](never/isdiscoverable.md)
  A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.
- [static var openAppWhenRun: Bool](never/openappwhenrun.md)
  A boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [static var parameterSummary: some ParameterSummary](never/parametersummary.md)
- [static var supportedModes: IntentModes](never/supportedmodes.md)
  Defines the supported modes that describe the behavior of your app intent.
- [static var title: LocalizedStringResource](never/title.md)
  A short, localized, human-readable string that describes the app intent using a verb and a noun in title case.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/appintent-implementations)*