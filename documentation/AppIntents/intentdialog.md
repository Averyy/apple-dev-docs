# IntentDialog

**Framework**: App Intents  
**Kind**: struct

The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct IntentDialog
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)

## Topics

### Creating a dialog
- [init(LocalizedStringResource)](intentdialog/init(_:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource)](intentdialog/init(full:supporting:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, systemImageName: String)](intentdialog/init(full:systemimagename:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource, systemImageName: String)](intentdialog/init(full:supporting:systemimagename:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [protocol OpensIntent](opensintent.md)
  A result type that indicates your app intent returns another app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdialog)*