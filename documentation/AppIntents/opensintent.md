# OpensIntent

**Framework**: App Intents  
**Kind**: protocol

The result of performing an action that delivers an app intent back to the initiator of the action.

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
protocol OpensIntent : IntentResult
```

## Relationships

### Inherits From
- [IntentResult](intentresult.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [IntentResultContainer](intentresultcontainer.md)

## See Also

- [protocol IntentResult](intentresult.md)
  A type that contains the result of performing an action, and includes optional information to deliver back to the initiator.
- [struct IntentResultContainer](intentresultcontainer.md)
  An object that represents the output of a completed intent.
- [protocol ProvidesDialog](providesdialog.md)
  The result of performing an action that delivers a dialog back to the initiator of the action.
- [protocol ReturnsValue](returnsvalue.md)
  The result of performing an action that delivers a value back to the initiator.
- [protocol ShowsSnippetView](showssnippetview.md)
  The result of performing an action that delivers a view back to the initiator of the action.
- [protocol ResultsCollection](resultscollection.md)
  A protocol representing a collection of returned items with support for sectioning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/opensintent)*