# startTracking(at:within:sourceImage:sourceDisparity:)

**Framework**: Cinematic  
**Kind**: method

Starts creating a detection track to track an object within the given bounds.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func startTracking(at time: CMTime, within normalizedBounds: CGRect, sourceImage: CVPixelBuffer, sourceDisparity: CVPixelBuffer) -> Bool
```

#### Return Value

A flag representing whether the object can be tracked.

#### Discussion

If you can track the object, the system adds a detection to the detection track you’re building.

## Parameters

- `time`: The presentation time of the first frame in the detection track.
- `normalizedBounds`: The bounds of the object to track in normalized coordinates where (0.0, 0.0) is the upper-left corner, and (1.0, 1.0) is the lower-right.
- `sourceImage`: The image buffer containing the image.
- `sourceDisparity`: The disparity buffer containing depth information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnobjecttracker-1n598/starttracking(at:within:sourceimage:sourcedisparity:))*