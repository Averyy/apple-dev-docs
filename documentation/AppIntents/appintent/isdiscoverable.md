# isDiscoverable

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static var isDiscoverable: Bool { get }
```

#### Discussion

App Intents must be discoverable to support App Shortcuts. If your app intent isn’t discoverable, people can use it only when it’s directly connected by a button in a SwiftUI app or a widget.

This property is `true` by default.

## See Also

- [static var title: LocalizedStringResource](appintent/title.md)
  A short, localized, human-readable string that describes the app intent using a verb and a noun in title case.
- [static var description: IntentDescription?](appintent/description.md)
  A description of the app intent that the system shows to people.
- [static var openAppWhenRun: Bool](appintent/openappwhenrun.md)
  A boolean property that tells the system to consider the app intent even if its app is not in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/isdiscoverable)*