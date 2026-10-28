# IntentResult

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

A type that contains the result of performing an action, and includes optional information to deliver back to the initiator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
protocol IntentResult : Sendable
```

## Overview

Instead of implementing this protocol, use the [`ReturnsValue`](./returnsvalue.md), [`OpensAppIntent`](./intentresult/opensappintent.md), [`ProvidesDialog`](./providesdialog.md), and [`ShowsSnippetView`](./showssnippetview.md) type aliases on your [`perform()`](./appintent/perform%28%29.md) implementation in combination with the [`result()`](./intentresult/result%28%29.md) methods as shown in the following example:

```swift
func perform() async throws -> some ReturnsValue<Int> & OpensAppIntent {
    .result(value: 1, opensIntent: MyOpensIntent())
}
```

## Topics

### Getting the result value
- [var value: Self.Value?](./intentresult/value-swift.property.md)
### Communicating the result to the user
- [associatedtype Dialog = Never](./intentresult/dialog.md)
### Associated Types
- [associatedtype OpensAppIntent : AppIntent = Never](./intentresult/opensappintent.md)
- [associatedtype Snippet = Never](./intentresult/snippet.md)
- [associatedtype Value : _IntentValue = Never](./intentresult/value-swift.associatedtype.md)
### Type Methods
- [static func result() -> Self](./intentresult/result%28%29.md)
  Indicates the `AppIntent` finished performing
- [static func result<Intent>(actionButtonIntent: Intent) -> Self](./intentresult/result%28actionbuttonintent%29.md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String) -> Self](./intentresult/result%28actionbuttonintent,activityidentifier%29.md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String, dialog: IntentDialog) -> Self](./intentresult/result%28actionbuttonintent,activityidentifier,dialog%29.md)
  Creates a result container with a follow-on intent, an identifier, and a dialog.
- [static func result<Intent>(actionButtonIntent: Intent, dialog: IntentDialog) -> Self](./intentresult/result%28actionbuttonintent,dialog%29.md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Content>(content: () -> Content) -> Self](./intentresult/result%28content%29.md)
  Indicates the `AppIntent` finished performing
- [static func result(dialog: IntentDialog) -> Self](./intentresult/result%28dialog%29.md)
  Indicates the `AppIntent` finished performing
- [static func result<Content>(dialog: IntentDialog, content: () -> Content) -> Self](./intentresult/result%28dialog,content%29.md)
  Indicates the `AppIntent` finished performing
- [static func result(dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](./intentresult/result%28dialog,snippetintent%29.md)
  Indicates that a completed app intent displays an interactive snippet and a success dialog.
- [static func result<Content>(dialog: IntentDialog, view: Content) -> Self](./intentresult/result%28dialog,view%29.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent) -> Self](./intentresult/result%28opensintent%29-8t8q8.md)
  Indicates the `AppIntent` finished performing
- [static func result<OpensAppIntent, Content>(opensIntent: OpensAppIntent, content: () -> Content) -> Self](./intentresult/result%28opensintent,content%29-2h5ux.md)
- [static func result<Content>(opensIntent: some AppIntent, content: () -> Content) -> Self](./intentresult/result%28opensintent,content%29-965vk.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent, dialog: IntentDialog) -> Self](./intentresult/result%28opensintent,dialog%29-64q5v.md)
  Indicates the `AppIntent` finished performing
- [static func result<OpensAppIntent, Content>(opensIntent: OpensAppIntent, dialog: IntentDialog, content: () -> Content) -> Self](./intentresult/result%28opensintent,dialog,content%29-2g81m.md)
- [static func result<Content>(opensIntent: some AppIntent, dialog: IntentDialog, content: () -> Content) -> Self](./intentresult/result%28opensintent,dialog,content%29-9kg66.md)
  Indicates the `AppIntent` finished performing
- [static func result(opensIntent: some AppIntent, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](./intentresult/result%28opensintent,dialog,snippetintent%29.md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns another intent to open the originating app.
- [static func result<Content>(opensIntent: some AppIntent, dialog: IntentDialog, view: Content) -> Self](./intentresult/result%28opensintent,dialog,view%29-1w6b6.md)
  Indicates the `AppIntent` finished performing
- [static func result<OpensAppIntent, Content>(opensIntent: OpensAppIntent, dialog: IntentDialog, view: Content) -> Self](./intentresult/result%28opensintent,dialog,view%29-8wkpg.md)
- [static func result(opensIntent: some AppIntent, snippetIntent: some SnippetIntent) -> Self](./intentresult/result%28opensintent,snippetintent%29.md)
  Indicates that a completed app intent displays an interactive snippet and returns another intent to open the originating app.
- [static func result<OpensAppIntent, Content>(opensIntent: OpensAppIntent, view: Content) -> Self](./intentresult/result%28opensintent,view%29-4l1d4.md)
- [static func result<Content>(opensIntent: some AppIntent, view: Content) -> Self](./intentresult/result%28opensintent,view%29-5hm2s.md)
  Indicates the `AppIntent` finished performing
- [static func result(snippetIntent: some SnippetIntent) -> Self](./intentresult/result%28snippetintent%29.md)
  Indicates that a completed app intent displays an interactive snippet.
- [static func result<Value>(value: Value) -> Self](./intentresult/result%28value%29.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent) -> Self](./intentresult/result%28value,actionbuttonintent%29.md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, activityIdentifier: String) -> Self](./intentresult/result%28value,actionbuttonintent,activityidentifier%29.md)
  Creates a result container with a value, a follow-on intent, and an identifier.
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, activityIdentifier: String, dialog: IntentDialog) -> Self](./intentresult/result%28value,actionbuttonintent,activityidentifier,dialog%29.md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, dialog: IntentDialog) -> Self](./intentresult/result%28value,actionbuttonintent,dialog%29.md)
  Indicates the Intent finished performing with an `AppIntent` to continue with
- [static func result<Value, Content>(value: Value, content: () -> Content) -> Self](./intentresult/result%28value,content%29.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, dialog: IntentDialog) -> Self](./intentresult/result%28value,dialog%29.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, Content>(value: Value, dialog: IntentDialog, content: () -> Content) -> Self](./intentresult/result%28value,dialog,content%29.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](./intentresult/result%28value,dialog,snippetintent%29.md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns a value.
- [static func result<Value, Content>(value: Value, dialog: IntentDialog, view: Content) -> Self](./intentresult/result%28value,dialog,view%29.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent) -> Self](./intentresult/result%28value,opensintent%29-8v5op.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, Content>(value: Value, opensIntent: some AppIntent, content: () -> Content) -> Self](./intentresult/result%28value,opensintent,content%29-2f6ht.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, OpensAppIntent, Content>(value: Value, opensIntent: OpensAppIntent, content: () -> Content) -> Self](./intentresult/result%28value,opensintent,content%29-95tmb.md)
- [static func result<Value>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog) -> Self](./intentresult/result%28value,opensintent,dialog%29-1eg3x.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, OpensAppIntent, Content>(value: Value, opensIntent: OpensAppIntent, dialog: IntentDialog, content: () -> Content) -> Self](./intentresult/result%28value,opensintent,dialog,content%29-4iwem.md)
- [static func result<Value, Content>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog, content: () -> Content) -> Self](./intentresult/result%28value,opensintent,dialog,content%29-mwwf.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog, snippetIntent: some SnippetIntent) -> Self](./intentresult/result%28value,opensintent,dialog,snippetintent%29.md)
  Indicates that a completed app intent displays an interactive snippet with a dialog and returns a value and another intent to open the originating app.
- [static func result<Value, OpensAppIntent, Content>(value: Value, opensIntent: OpensAppIntent, dialog: IntentDialog, view: Content) -> Self](./intentresult/result%28value,opensintent,dialog,view%29-5sg4p.md)
- [static func result<Value, Content>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog, view: Content) -> Self](./intentresult/result%28value,opensintent,dialog,view%29-88j6a.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value>(value: Value, opensIntent: some AppIntent, snippetIntent: some SnippetIntent) -> Self](./intentresult/result%28value,opensintent,snippetintent%29.md)
  Indicates that a completed app intent displays an interactive snippet and returns a value and another intent to open the originating app.
- [static func result<Value, Content>(value: Value, opensIntent: some AppIntent, view: Content) -> Self](./intentresult/result%28value,opensintent,view%29-12wbo.md)
  Indicates the `AppIntent` finished performing
- [static func result<Value, OpensAppIntent, Content>(value: Value, opensIntent: OpensAppIntent, view: Content) -> Self](./intentresult/result%28value,opensintent,view%29-5z5t0.md)
- [static func result<Value>(value: Value, snippetIntent: some SnippetIntent) -> Self](./intentresult/result%28value,snippetintent%29.md)
  Indicates that a completed app intent returns a value and displays an interactive snippet.
- [static func result<Value, Content>(value: Value, view: Content) -> Self](./intentresult/result%28value,view%29.md)
  Indicates the `AppIntent` finished performing
- [static func result<Content>(view: Content) -> Self](./intentresult/result%28view%29.md)
  Indicates the `AppIntent` finished performing
### Default Implementations
- [IntentResult Implementations](./intentresult/intentresult-implementations.md)

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Inherited By
- [OpensIntent](./opensintent.md)
- [ProvidesDialog](./providesdialog.md)
- [ReturnsValue](./returnsvalue.md)
- [ShowsSnippetIntent](./showssnippetintent.md)
- [ShowsSnippetView](./showssnippetview.md)
### Conforming Types
- [IntentResultContainer](./intentresultcontainer.md)

## See Also

### Results
- [struct IntentDialog](./intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [struct IntentResultContainer](./intentresultcontainer.md)
  An object that represents the output of a completed intent.
- [protocol ProvidesDialog](./providesdialog.md)
  The result of performing an action that delivers a dialog back to the initiator of the action.
- [protocol ReturnsValue](./returnsvalue.md)
  The result of performing an action that delivers a value back to the initiator.
- [protocol ShowsSnippetView](./showssnippetview.md)
  The result of performing an action that delivers a view back to the initiator of the action.
- [protocol ResultsCollection](./resultscollection.md)
  A protocol representing a collection of returned items with support for sectioning.
- [protocol OpensIntent](./opensintent.md)
  A result type that indicates your app intent returns another app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult)*