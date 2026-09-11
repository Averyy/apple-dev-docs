# init(local:stable:)

**Framework**: App Intents  
**Kind**: init

Creates an identifier with both local and stable IDs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(local: LocalID, stable: StableID)
```

#### Discussion

Use this initializer when you use separate local and stable identifiers to refer to your entity.

## Parameters

- `local`: The device-specific identifier
- `stable`: The cross-device stable identifier


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/init(local:stable:))*