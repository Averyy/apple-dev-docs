# documentLaunchSubtitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the subtitle displayed beneath the title on the document launch card, using a string.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
nonisolated
func documentLaunchSubtitle<S>(_ subtitle: S) -> some View where S : StringProtocol
```

**Other overloads**:

```swift
nonisolated
func documentLaunchSubtitle(_ subtitle: Text) -> some View
```

```swift
nonisolated
func documentLaunchSubtitle(_ subtitleKey: LocalizedStringKey) -> some View
```

```swift
nonisolated
func documentLaunchSubtitle(_ subtitleResource: LocalizedStringResource) -> some View
```

## Parameters

- `subtitle`: The string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/documentlaunchsubtitle(_:)-4can9)*