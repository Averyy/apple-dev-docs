# QualityOfService.utility

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case utility
```

```c
NSQualityOfServiceUtility
```

#### Discussion

Used for performing work which the user is unlikely to be immediately waiting for the results. This work may have been requested by the user or initiated automatically, and often operates at user-visible timescales using a non-modal progress indicator. For example, periodic content updates or bulk file operations, such as media import.

## See Also

### Constants
- [QualityOfService.userInteractive](./userinteractive.md)
- [QualityOfService.userInitiated](./userinitiated.md)
- [QualityOfService.background](./background.md)
- [QualityOfService.default](./default.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/qualityofservice/utility)*