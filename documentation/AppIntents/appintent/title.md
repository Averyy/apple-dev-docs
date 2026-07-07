# title

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

A short, localized, human-readable string that conveys the app intent’s action.

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
static var title: LocalizedStringResource { get }
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Creating your first app intent](creating-your-first-app-intent.md)

#### Discussion

Specify title strings using a verb followed by a noun in title case. For example, an action to open an album might have the title “Open Album”. If the app intent conforms to a schema, the schema provides this value.

## See Also

- [static var description: IntentDescription?](appintent/description.md)
  A localized string that describes what the app intent does.
- [static var isDiscoverable: Bool](appintent/isdiscoverable.md)
  A Boolean value that indicates whether system features can discover this app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/title)*