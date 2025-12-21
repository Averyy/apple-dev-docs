# IntentDescription

**Framework**: App Intents  
**Kind**: struct

The human-readable description and metadata for an app intent.

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
struct IntentDescription
```

## Topics

### Creating a description
- [init(LocalizedStringResource, categoryName: LocalizedStringResource?, searchKeywords: [LocalizedStringResource])](intentdescription/init(_:categoryname:searchkeywords:).md)
### Initializers
- [init(LocalizedStringResource, categoryName: LocalizedStringResource?, searchKeywords: [LocalizedStringResource], resultValueName: LocalizedStringResource?)](intentdescription/init(_:categoryname:searchkeywords:resultvaluename:).md)
### Instance Properties
- [var categoryName: LocalizedStringResource?](intentdescription/categoryname.md)
  The category in which this intent will be grouped into in the Shortcuts editor.
- [var descriptionText: LocalizedStringResource](intentdescription/descriptiontext.md)
  A short, localized, human-readable string that describes the intent using sentence case and followed by a period.
- [var resultValueName: LocalizedStringResource?](intentdescription/resultvaluename.md)
  A name for the result of this intent, which will be displayed in the Shortcuts editor, such as when the output is used as a variable.
- [var searchKeywords: [LocalizedStringResource]](intentdescription/searchkeywords.md)
  A set of keywords which, when searched in the Shortcuts editor, will reveal this intent.

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AppIntentsPackage](appintentspackage.md)
  A type that describes app intent definitions that aren’t part of an app bundle and their dependencies.
- [struct IntentDialog](intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [struct IntentDeprecation](intentdeprecation.md)
- [class IntentProjection](intentprojection.md)
  Projections for an app intent that returns non-optional values for parameters.
- [struct IntentSystemContext](intentsystemcontext.md)
  Information that the system makes available to an app intent while it performs its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdescription)*