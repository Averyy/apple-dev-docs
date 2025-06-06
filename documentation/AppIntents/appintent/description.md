# description

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

A description of the app intent that the system shows to people.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var description: IntentDescription? { get }
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)

## See Also

- [static var title: LocalizedStringResource](appintent/title.md)
  A short, localized, human-readable string that describes the app intent using a verb and a noun in title case.
- [static var openAppWhenRun: Bool](appintent/openappwhenrun.md)
  A boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [static var isDiscoverable: Bool](appintent/isdiscoverable.md)
  A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/description)*