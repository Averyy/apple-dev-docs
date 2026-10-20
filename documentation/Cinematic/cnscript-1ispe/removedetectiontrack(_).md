# removeDetectionTrack(_:)

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Removes the user-created detection track.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final func removeDetectionTrack(_ detectionTrack: CNDetectionTrack) -> Bool
```

#### Return Value

A flag indicating whether removal of the user-created detection track was successful.

#### Discussion

It’s not possible to remove tracks created at recording time.

## Parameters

- `detectionTrack`: The detection track to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/removedetectiontrack(_:))*