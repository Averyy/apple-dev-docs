# accessibilityScrollStatus(_:isEnabled:)

**Framework**: App Intents  
**Kind**: method

Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func accessibilityScrollStatus(_ status: Text, isEnabled: Bool = true) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this modifier to provide a description of the content at the current position in the scroll view. For example, you could use this modifier to announce the current month being scrolled to in a view that contains a calendar.

ScrollView { LazyVStack { ForEach(months) { months in MonthView(month: months) } } .scrollTargetLayout() } .scrollPosition($position) .accessibilityScrollStatus(”(months.name(position.viewID)) (year)”)

By default, VoiceOver announces “Page X of Y” while scrolling.

## Parameters

- `status`: The current status of the scroll view.
- `isEnabled`: If true the accessibility scroll status is applied;   otherwise the accessibility scroll status is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/accessibilityscrollstatus(_:isenabled:)-8gvyg)*