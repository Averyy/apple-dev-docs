# IntentResultContainer

**Framework**: App Intents  
**Kind**: struct

An object that represents the output of a completed intent.

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
struct IntentResultContainer<Value, OpensAppIntent, Snippet, Dialog> where Value : _IntentValue, OpensAppIntent : AppIntent
```

#### Overview

Use the `IntentResult.result()` family of functions to create instances

## Topics

### Instance Properties
- [var activityIdentifier: String?](intentresultcontainer/activityidentifier.md)
- [var dialog: IntentDialog?](intentresultcontainer/dialog.md)
- [var opensIntent: OpensAppIntent?](intentresultcontainer/opensintent.md)
- [var value: Value?](intentresultcontainer/value.md)
### Default Implementations
- [IntentResult Implementations](intentresultcontainer/intentresult-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [IntentResult](intentresult.md)
- [OpensIntent](opensintent.md)
- [ProvidesDialog](providesdialog.md)
- [ReturnsValue](returnsvalue.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [ShowsSnippetIntent](showssnippetintent.md)
- [ShowsSnippetView](showssnippetview.md)

## See Also

- [protocol IntentResult](intentresult.md)
  A type that contains the result of performing an action, and includes optional information to deliver back to the initiator.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresultcontainer)*