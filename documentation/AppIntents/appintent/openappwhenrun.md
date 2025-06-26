# openAppWhenRun

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

A boolean property that tells the system to consider the app intent even if its app is not in the foreground.

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
static var openAppWhenRun: Bool { get }
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Creating your first app intent](creating-your-first-app-intent.md)

#### Discussion

This property is deprecated, use [`supportedModes`](appintent/supportedmodes.md) instead. For backward compatibility, provide `openAppWhenRun` in an extension, for example:

```swift
@available(*, deprecated)
extension OrderSoupIntent {
    static var openAppWhenRun: Bool { true }
}
```

## See Also

- [static var title: LocalizedStringResource](appintent/title.md)
  A short, localized, human-readable string that describes the app intent using a verb and a noun in title case.
- [static var description: IntentDescription?](appintent/description.md)
  A description of the app intent that the system shows to people.
- [static var isDiscoverable: Bool](appintent/isdiscoverable.md)
  A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/openappwhenrun)*