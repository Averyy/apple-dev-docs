# level

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The guidance for the model to use during a session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let level: SpotlightSearchTool.GuidanceLevel
```

## Discussion

Use this property to specify custom guidance for how to search your app’s content. The default value of this property is [`SpotlightSearchTool.GuidanceLevel.complete`](../guidancelevel/complete.md), which uses all available search techniques and search all content types.

## See Also

### Getting the guidance
- [let format: SpotlightSearchTool.FormatLevel](./format.md)
  The representation format for tool responses returned to the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/guide/level)*