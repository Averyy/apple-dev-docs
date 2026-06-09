# selectableMediaSelectionOptions(in:)

**Framework**: AVFoundation  
**Kind**: method

Returns the media selection options in the specified media selection group that can produce content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func selectableMediaSelectionOptions(in mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaSelectionOption]
```

#### Return Value

An array containing the media selection options from the group that can produce content. Options in the group that are not in this array can still be selected, but will produce no content.

#### Discussion

Some media selection options depend on other options to produce content. For example, a subtitle option generated via audio transcription may require that the source audio option is currently selected. This method filters the options in the specified group to only those that can produce content given the current state of the player item’s media selection.

## Parameters

- `mediaSelectionGroup`: A media selection group obtained from the receiver’s asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/selectablemediaselectionoptions(in:))*