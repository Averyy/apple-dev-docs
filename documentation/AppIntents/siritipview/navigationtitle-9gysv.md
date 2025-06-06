# navigationTitle(_:)

**Framework**: App Intents  
**Kind**: method

Configures the view’s title for purposes of navigation, using a string binding.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationTitle(_ title: Binding<String>) -> some View
```

#### Discussion

In iOS, iPadOS, and macOS, this allows editing the navigation title when the title is displayed in the toolbar.

Refer to the doc:Configure-Your-Apps-Navigation-Titles article for more information on navigation title modifiers.

## Parameters

- `title`: The text of the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/navigationtitle(_:)-9gysv)*