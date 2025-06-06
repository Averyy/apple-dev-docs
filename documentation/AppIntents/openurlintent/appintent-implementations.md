# AppIntent Implementations

**Framework**: App Intents

## Topics

### Instance Properties
- [var systemContext: IntentSystemContext](openurlintent/systemcontext.md)
  Context information that’s available while the system performs the app intent’s action.
### Instance Methods
- [func callAsFunction(donate: Bool) async throws](openurlintent/callasfunction(donate:)-6emik.md)
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](openurlintent/callasfunction(donate:)-74ri4.md)
- [func donate() -> IntentDonationIdentifier](openurlintent/donate-981xn.md)
  Donates the intent to the transcript.
- [func donate() async throws -> IntentDonationIdentifier](openurlintent/donate-d5p6.md)
  Donates the intent to the transcript.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](openurlintent/donate(result:)-89co.md)
  Donates the intent and optional result to the transcript.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](openurlintent/donate(result:)-pm6e.md)
  Donates the intent and optional result to the transcript.
- [func requestConfirmation() async throws](openurlintent/requestconfirmation.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](openurlintent/requestconfirmation(conditions:actionname:dialog:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](openurlintent/requestconfirmation(output:confirmationactionname:showprompt:).md)
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](openurlintent/requestconfirmation(result:confirmationactionname:showprompt:).md)
  Requests user confirmation before performing the app intent.
### Type Aliases
- [OpenURLIntent.Case](openurlintent/case.md)
- [OpenURLIntent.DefaultCase](openurlintent/defaultcase.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/appintent-implementations)*