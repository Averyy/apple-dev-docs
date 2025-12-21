# foreground(_:)

**Framework**: App Intents  
**Kind**: method

Creates and returns a foreground mode with a specified behavior.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func foreground(_ foregroundMode: IntentModes.ForegroundMode) -> IntentModes
```

#### Return Value

A set of options that describes the specified foreground behavior.

## Parameters

- `foregroundMode`: The specific foreground behavior; for example,   to immediately   bring the app into the foreground and then perform the app intent’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/foreground(_:))*