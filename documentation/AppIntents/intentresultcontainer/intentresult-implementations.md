# IntentResult Implementations

**Framework**: App Intents

## Topics

### Type Methods
- [static func result() -> Self](intentresultcontainer/result.md)
  Indicates the `AppIntent` finished performing
- [static func result<Intent>(actionButtonIntent: Intent) -> Self](intentresultcontainer/result(actionbuttonintent:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String) -> Self](intentresultcontainer/result(actionbuttonintent:activityidentifier:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String, dialog: IntentDialog) -> Self](intentresultcontainer/result(actionbuttonintent:activityidentifier:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, dialog: IntentDialog) -> Self](intentresultcontainer/result(actionbuttonintent:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result(dialog: IntentDialog) -> Self](intentresultcontainer/result(dialog:).md)
  Indicates the `AppIntent` finished performing
- [static func result(dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](intentresultcontainer/result(dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet and a success dialog.
- [static func result<OpensAppIntent>(opensIntent: OpensAppIntent) -> Self](intentresultcontainer/result(opensintent:)-2an32.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent) -> Self](intentresultcontainer/result(opensintent:)-7k5p4.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent, dialog: IntentDialog) -> Self](intentresultcontainer/result(opensintent:dialog:)-4znom.md)
  Indicates the `AppIntent` finished performing
- [static func result<OpensAppIntent>(opensIntent: OpensAppIntent, dialog: IntentDialog) -> Self](intentresultcontainer/result(opensintent:dialog:)-6wf55.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](intentresultcontainer/result(opensintent:dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns another intent to open the originating app.
- [static func result(opensIntent: some AppIntent, snippetIntent: some SnippetIntent) -> Self](intentresultcontainer/result(opensintent:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet and returns another intent to open the originating app.
- [static func result(snippetIntent: some SnippetIntent) -> Self](intentresultcontainer/result(snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet.
- [static func result<Value>(value: Value) -> Self](intentresultcontainer/result(value:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent) -> Self](intentresultcontainer/result(value:actionbuttonintent:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, activityIdentifier: String) -> Self](intentresultcontainer/result(value:actionbuttonintent:activityidentifier:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, activityIdentifier: String, dialog: IntentDialog) -> Self](intentresultcontainer/result(value:actionbuttonintent:activityidentifier:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, dialog: IntentDialog) -> Self](intentresultcontainer/result(value:actionbuttonintent:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value>(value: Value, dialog: IntentDialog) -> Self](intentresultcontainer/result(value:dialog:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](intentresultcontainer/result(value:dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns a value.
- [static func result<Value>(value: Value, opensIntent: some AppIntent) -> Self](intentresultcontainer/result(value:opensintent:)-40le.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, OpensAppIntent>(value: Value, opensIntent: OpensAppIntent) -> Self](intentresultcontainer/result(value:opensintent:)-8g6rp.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog) -> Self](intentresultcontainer/result(value:opensintent:dialog:)-6he5w.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, OpensAppIntent>(value: Value, opensIntent: OpensAppIntent, dialog: IntentDialog) -> Self](intentresultcontainer/result(value:opensintent:dialog:)-7ghvc.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](intentresultcontainer/result(value:opensintent:dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns a value and another intent to open the originating app.
- [static func result<Value>(value: Value, opensIntent: some AppIntent, snippetIntent: some SnippetIntent) -> Self](intentresultcontainer/result(value:opensintent:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet and returns a value and another intent to open the originating app.
- [static func result<Value>(value: Value, snippetIntent: some SnippetIntent) -> Self](intentresultcontainer/result(value:snippetintent:).md)
  Indicates that a completed app intent returns a value and displays an interactive snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresultcontainer/intentresult-implementations)*