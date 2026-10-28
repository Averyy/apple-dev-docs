# documentLaunchTitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the title displayed on the document launch card, using a localized string resource.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
nonisolated
func documentLaunchTitle(_ titleResource: LocalizedStringResource) -> some Scene
```

**Other overloads**:

```swift
nonisolated
func documentLaunchTitle(_ title: Text) -> some Scene
```

```swift
nonisolated
func documentLaunchTitle(_ titleKey: LocalizedStringKey) -> some Scene
```

```swift
nonisolated
func documentLaunchTitle<S>(_ title: S) -> some Scene where S : StringProtocol
```

## Parameters

- `titleResource`: The resource to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/documentlaunchtitle(_:)-59hz7)*