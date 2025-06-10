# undoManager

**Framework**: App Intents  
**Kind**: property

An app intent’s `perform` method should use this undo manager to register operations that undo the effect of the app intent’s performance

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
@MainActor
var undoManager: UndoManager? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/undoableintent/undomanager)*