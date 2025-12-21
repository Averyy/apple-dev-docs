# init(maximumDescriptions:)

**Framework**: Core Audio  
**Kind**: init

Creates a new `ManagedAudioChannelLayout` that can hold up to `maximumDescriptions`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
init(maximumDescriptions: Int)
```

#### Discussion

Use `ManagedAudioChannelLayout(tag:)` if no `AudioChannelDescription` are needed.

## Parameters

- `maximumDescriptions`: The maximum number of    this   can hold.   This must be greater than  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/managedaudiochannellayout/init(maximumdescriptions:))*