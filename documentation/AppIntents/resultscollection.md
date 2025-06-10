# ResultsCollection

**Framework**: App Intents  
**Kind**: protocol

A protocol representing a collection of returned items with support for sectioning.

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
protocol ResultsCollection<Result>
```

## Topics

### Associated Types
- [associatedtype Result : _IntentValue](resultscollection/result.md)
### Instance Properties
- [var items: [Self.Result.ValueType]](resultscollection/items.md)
  All result items.
- [var promptLabel: LocalizedStringResource?](resultscollection/promptlabel.md)
  A text prompt shown at the top of the view that presents the options.
- [var usesIndexedCollation: Bool](resultscollection/usesindexedcollation.md)
  If set to true, presents the list of options with an alphabetical index on the right side of the screen (table view section index titles).
### Type Properties
- [static var empty: Self](resultscollection/empty.md)
  An empty result.

## Relationships

### Conforming Types
- [IntentItemCollection](intentitemcollection.md)

## See Also

- [protocol IntentResult](intentresult.md)
  A type that contains the result of performing an action, and includes optional information to deliver back to the initiator.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resultscollection)*