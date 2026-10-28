# documentLaunchSubtitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the subtitle displayed beneath the title on the document launch card, using a localized string key.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
nonisolated
func documentLaunchSubtitle(_ subtitleKey: LocalizedStringKey) -> some Scene
```

**Other overloads**:

```swift
nonisolated
func documentLaunchSubtitle(_ subtitle: Text) -> some Scene
```

```swift
nonisolated
func documentLaunchSubtitle(_ subtitleResource: LocalizedStringResource) -> some Scene
```

```swift
nonisolated
func documentLaunchSubtitle<S>(_ subtitle: S) -> some Scene where S : StringProtocol
```

## Parameters

- `subtitleKey`: The key to a localized string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/documentlaunchsubtitle(_:)-5d5gq)*