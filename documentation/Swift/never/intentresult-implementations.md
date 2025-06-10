# IntentResult Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var value: Never?](never/value-swift.property.md)
### Type Aliases
- [typealias Dialog](never/dialog.md)
- [typealias OpensAppIntent](never/opensappintent.md)
- [typealias Snippet](never/snippet.md)
- [typealias Value](never/value-swift.typealias.md)
### Type Methods
- [static func result() -> Self](never/result.md)
  Indicates the `AppIntent` finished performing
- [static func result<Intent>(actionButtonIntent: Intent) -> Self](never/result(actionbuttonintent:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String) -> Self](never/result(actionbuttonintent:activityidentifier:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String, dialog: IntentDialog) -> Self](never/result(actionbuttonintent:activityidentifier:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, dialog: IntentDialog) -> Self](never/result(actionbuttonintent:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result(dialog: IntentDialog) -> Self](never/result(dialog:).md)
  Indicates the `AppIntent` finished performing
- [static func result(dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](never/result(dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet and a success dialog.
- [static func result<OpensAppIntent>(opensIntent: OpensAppIntent) -> Self](never/result(opensintent:)-6dbqd.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent) -> Self](never/result(opensintent:)-7ntvd.md)
  Indicates the `AppIntent` finished performing
- [static func result<OpensAppIntent>(opensIntent: OpensAppIntent, dialog: IntentDialog) -> Self](never/result(opensintent:dialog:)-73u1.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent, dialog: IntentDialog) -> Self](never/result(opensintent:dialog:)-8a1z1.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](never/result(opensintent:dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns another intent to open the originating app.
- [static func result(opensIntent: some AppIntent, snippetIntent: some SnippetIntent) -> Self](never/result(opensintent:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet and returns another intent to open the originating app.
- [static func result(snippetIntent: some SnippetIntent) -> Self](never/result(snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet.
- [static func result<Value>(value: Value) -> Self](never/result(value:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent) -> Self](never/result(value:actionbuttonintent:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, activityIdentifier: String) -> Self](never/result(value:actionbuttonintent:activityidentifier:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, activityIdentifier: String, dialog: IntentDialog) -> Self](never/result(value:actionbuttonintent:activityidentifier:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, dialog: IntentDialog) -> Self](never/result(value:actionbuttonintent:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value>(value: Value, dialog: IntentDialog) -> Self](never/result(value:dialog:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](never/result(value:dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns a value.
- [static func result<Value, OpensAppIntent>(value: Value, opensIntent: OpensAppIntent) -> Self](never/result(value:opensintent:)-44gwk.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent) -> Self](never/result(value:opensintent:)-7awmd.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog) -> Self](never/result(value:opensintent:dialog:)-1cbxz.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, OpensAppIntent>(value: Value, opensIntent: OpensAppIntent, dialog: IntentDialog) -> Self](never/result(value:opensintent:dialog:)-cm5q.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](never/result(value:opensintent:dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns a value and another intent to open the originating app.
- [static func result<Value>(value: Value, opensIntent: some AppIntent, snippetIntent: some SnippetIntent) -> Self](never/result(value:opensintent:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet and returns a value and another intent to open the originating app.
- [static func result<Value>(value: Value, snippetIntent: some SnippetIntent) -> Self](never/result(value:snippetintent:).md)
  Indicates that a completed app intent returns a value and displays an interactive snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/intentresult-implementations)*