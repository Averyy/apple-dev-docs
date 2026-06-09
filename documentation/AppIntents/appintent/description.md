# description

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

A localized string that describes what the app intent does.

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
static var description: IntentDescription? { get }
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)

#### Discussion

If the app intent conforms to a schema, the schema provides a default implementation and value. If you implement this property, the system uses your custom value instead of the default value.

## See Also

- [static var title: LocalizedStringResource](appintent/title.md)
  A short, localized, human-readable string that conveys the app intent’s action.
- [static var isDiscoverable: Bool](appintent/isdiscoverable.md)
  A Boolean value that indicates whether system features can discover this app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/description)*