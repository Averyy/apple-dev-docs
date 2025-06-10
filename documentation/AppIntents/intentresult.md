# IntentResult

**Framework**: App Intents  
**Kind**: protocol

A type that contains the result of performing an action, and includes optional information to deliver back to the initiator.

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
protocol IntentResult : Sendable
```

#### Overview

Instead of implementing this protocol, use the [`ReturnsValue`](returnsvalue.md), [`OpensAppIntent`](intentresult/opensappintent.md), [`ProvidesDialog`](providesdialog.md), and [`ShowsSnippetView`](showssnippetview.md) type aliases on your [`perform()`](appintent/perform().md) implementation in combination with the [`result()`](intentresult/result().md) methods as shown in the following example:

```swift
func perform() async throws -> some ReturnsValue<Int> & OpensAppIntent {
    .result(value: 1, opensIntent: MyOpensIntent())
}
```

## Topics

### Getting the result value
- [var value: Self.Value?](intentresult/value-swift.property.md)
### Communicating the result to the user
- [associatedtype Dialog = Never](intentresult/dialog.md)
### Associated Types
- [associatedtype OpensAppIntent : AppIntent = Never](intentresult/opensappintent.md)
- [associatedtype Snippet = Never](intentresult/snippet.md)
- [associatedtype Value : _IntentValue = Never](intentresult/value-swift.associatedtype.md)
### Type Methods
- [static func result() -> Self](intentresult/result.md)
  Indicates the `AppIntent` finished performing
- [static func result<Intent>(actionButtonIntent: Intent) -> Self](intentresult/result(actionbuttonintent:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String) -> Self](intentresult/result(actionbuttonintent:activityidentifier:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String, dialog: IntentDialog) -> Self](intentresult/result(actionbuttonintent:activityidentifier:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, dialog: IntentDialog) -> Self](intentresult/result(actionbuttonintent:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Content>(content: () -> Content) -> Self](intentresult/result(content:).md)
  Indicates the `AppIntent` finished performing
- [static func result(dialog: IntentDialog) -> Self](intentresult/result(dialog:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Content>(dialog: IntentDialog, content: () -> Content) -> Self](intentresult/result(dialog:content:).md)
  Indicates the `AppIntent` finished performing
- [static func result(dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](intentresult/result(dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet and a success dialog.
- [static func result<Content>(dialog: IntentDialog, view: Content) -> Self](intentresult/result(dialog:view:).md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent) -> Self](intentresult/result(opensintent:)-8t8q8.md)
  Indicates the `AppIntent` finished performing
- [static func result<OpensAppIntent, Content>(opensIntent: OpensAppIntent, content: () -> Content) -> Self](intentresult/result(opensintent:content:)-2h5ux.md)
- [static func result<Content>(opensIntent: some AppIntent, content: () -> Content) -> Self](intentresult/result(opensintent:content:)-965vk.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent, dialog: IntentDialog) -> Self](intentresult/result(opensintent:dialog:)-64q5v.md)
  Indicates the `AppIntent` finished performing
- [static func result<OpensAppIntent, Content>(opensIntent: OpensAppIntent, dialog: IntentDialog, content: () -> Content) -> Self](intentresult/result(opensintent:dialog:content:)-2g81m.md)
- [static func result<Content>(opensIntent: some AppIntent, dialog: IntentDialog, content: () -> Content) -> Self](intentresult/result(opensintent:dialog:content:)-9kg66.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](intentresult/result(opensintent:dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns another intent to open the originating app.
- [static func result<Content>(opensIntent: some AppIntent, dialog: IntentDialog, view: Content) -> Self](intentresult/result(opensintent:dialog:view:)-1w6b6.md)
  Indicates the `AppIntent` finished performing
- [static func result<OpensAppIntent, Content>(opensIntent: OpensAppIntent, dialog: IntentDialog, view: Content) -> Self](intentresult/result(opensintent:dialog:view:)-8wkpg.md)
- [static func result(opensIntent: some AppIntent, snippetIntent: some SnippetIntent) -> Self](intentresult/result(opensintent:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet and returns another intent to open the originating app.
- [static func result<OpensAppIntent, Content>(opensIntent: OpensAppIntent, view: Content) -> Self](intentresult/result(opensintent:view:)-4l1d4.md)
- [static func result<Content>(opensIntent: some AppIntent, view: Content) -> Self](intentresult/result(opensintent:view:)-5hm2s.md)
  Indicates the `AppIntent` finished performing
- [static func result(snippetIntent: some SnippetIntent) -> Self](intentresult/result(snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet.
- [static func result<Value>(value: Value) -> Self](intentresult/result(value:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent) -> Self](intentresult/result(value:actionbuttonintent:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, activityIdentifier: String) -> Self](intentresult/result(value:actionbuttonintent:activityidentifier:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, activityIdentifier: String, dialog: IntentDialog) -> Self](intentresult/result(value:actionbuttonintent:activityidentifier:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, dialog: IntentDialog) -> Self](intentresult/result(value:actionbuttonintent:dialog:).md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Content>(value: Value, content: () -> Content) -> Self](intentresult/result(value:content:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, dialog: IntentDialog) -> Self](intentresult/result(value:dialog:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, Content>(value: Value, dialog: IntentDialog, content: () -> Content) -> Self](intentresult/result(value:dialog:content:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](intentresult/result(value:dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns a value.
- [static func result<Value, Content>(value: Value, dialog: IntentDialog, view: Content) -> Self](intentresult/result(value:dialog:view:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent) -> Self](intentresult/result(value:opensintent:)-8v5op.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, Content>(value: Value, opensIntent: some AppIntent, content: () -> Content) -> Self](intentresult/result(value:opensintent:content:)-2f6ht.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, OpensAppIntent, Content>(value: Value, opensIntent: OpensAppIntent, content: () -> Content) -> Self](intentresult/result(value:opensintent:content:)-95tmb.md)
- [static func result<Value>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog) -> Self](intentresult/result(value:opensintent:dialog:)-1eg3x.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, OpensAppIntent, Content>(value: Value, opensIntent: OpensAppIntent, dialog: IntentDialog, content: () -> Content) -> Self](intentresult/result(value:opensintent:dialog:content:)-4iwem.md)
- [static func result<Value, Content>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog, content: () -> Content) -> Self](intentresult/result(value:opensintent:dialog:content:)-mwwf.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](intentresult/result(value:opensintent:dialog:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns a value and another intent to open the originating app.
- [static func result<Value, OpensAppIntent, Content>(value: Value, opensIntent: OpensAppIntent, dialog: IntentDialog, view: Content) -> Self](intentresult/result(value:opensintent:dialog:view:)-5sg4p.md)
- [static func result<Value, Content>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog, view: Content) -> Self](intentresult/result(value:opensintent:dialog:view:)-88j6a.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent, snippetIntent: some SnippetIntent) -> Self](intentresult/result(value:opensintent:snippetintent:).md)
  Indicates that a completed app intent displays an interactive snippet and returns a value and another intent to open the originating app.
- [static func result<Value, Content>(value: Value, opensIntent: some AppIntent, view: Content) -> Self](intentresult/result(value:opensintent:view:)-12wbo.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, OpensAppIntent, Content>(value: Value, opensIntent: OpensAppIntent, view: Content) -> Self](intentresult/result(value:opensintent:view:)-5z5t0.md)
- [static func result<Value>(value: Value, snippetIntent: some SnippetIntent) -> Self](intentresult/result(value:snippetintent:).md)
  Indicates that a completed app intent returns a value and displays an interactive snippet.
- [static func result<Value, Content>(value: Value, view: Content) -> Self](intentresult/result(value:view:).md)
  Indicates the `AppIntent` finished performing
- [static func result<Content>(view: Content) -> Self](intentresult/result(view:).md)
  Indicates the `AppIntent` finished performing
### Default Implementations
- [IntentResult Implementations](intentresult/intentresult-implementations.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [OpensIntent](opensintent.md)
- [ProvidesDialog](providesdialog.md)
- [ReturnsValue](returnsvalue.md)
- [ShowsSnippetIntent](showssnippetintent.md)
- [ShowsSnippetView](showssnippetview.md)
### Conforming Types
- [IntentResultContainer](intentresultcontainer.md)

## See Also

- [struct IntentResultContainer](intentresultcontainer.md)
  An object that represents the output of a completed intent.
- [protocol OpensIntent](opensintent.md)
  The result of performing an action that delivers an app intent back to the initiator of the action.
- [protocol ProvidesDialog](providesdialog.md)
  The result of performing an action that delivers a dialog back to the initiator of the action.
- [protocol ReturnsValue](returnsvalue.md)
  The result of performing an action that delivers a value back to the initiator.
- [protocol ShowsSnippetView](showssnippetview.md)
  The result of performing an action that delivers a view back to the initiator of the action.
- [protocol ResultsCollection](resultscollection.md)
  A protocol representing a collection of returned items with support for sectioning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult)*