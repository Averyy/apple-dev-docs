# speechAnnouncementsQueued(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func speechAnnouncementsQueued(_ value: Bool = true) -> some View
```

#### Discussion

Use this modifier when you want affect the order in which the accessibility system delivers spoken text. Announcements can occur automatically when the label or value of an accessibility element changes.

## Parameters

- `value`: A Boolean value that determines if VoiceOver speaks   changes to text immediately or enqueues them behind existing speech.   Defaults to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/speechannouncementsqueued(_:))*