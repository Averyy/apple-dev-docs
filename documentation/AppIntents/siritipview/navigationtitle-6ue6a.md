# navigationTitle(_:)

**Framework**: App Intents  
**Kind**: method

Configures the view’s title for purposes of navigation, using a localized string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationTitle(_ titleResource: LocalizedStringResource) -> some View
```

#### Discussion

A view’s navigation title is used to visually display the current navigation state of an interface. On iOS and watchOS, when a view is navigated to inside of a navigation view, that view’s title is displayed in the navigation bar. On iPadOS, the primary destination’s navigation title is reflected as the window’s title in the App Switcher. Similarly on macOS, the primary destination’s title is used as the window title in the titlebar, Windows menu and Mission Control.

Refer to the doc:Configure-Your-Apps-Navigation-Titles article for more information on navigation title modifiers.

## Parameters

- `titleResource`: The key to a localized string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/navigationtitle(_:)-6ue6a)*