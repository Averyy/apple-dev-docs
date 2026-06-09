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

A set of options that describes the foreground behavior.

## Parameters

- `foregroundMode`: The foreground behavior to apply to the app intent. For example, specify [`immediate`](intentmodes/foregroundmode/immediate.md) to bring the app to the foreground before running the app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/foreground(_:))*