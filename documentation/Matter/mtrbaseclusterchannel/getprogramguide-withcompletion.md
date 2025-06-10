# getProgramGuide(with:completion:)

**Framework**: Matter  
**Kind**: method

Command GetProgramGuide

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func programGuide(with params: MTRChannelClusterGetProgramGuideParams?) async throws -> MTRChannelClusterProgramGuideResponseParams
```

#### Discussion

This command retrieves the program guide. It accepts several filter parameters to return specific schedule and program information from a content app. The command shall receive in response a ProgramGuideResponse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterchannel/getprogramguide(with:completion:))*