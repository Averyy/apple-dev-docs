# BEGestureType

**Framework**: BrowserEngineKit  
**Kind**: enum

The types of touch gestures that operate on input text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
enum BEGestureType
```

## Topics

### Tap gestures
- [BEGestureType.oneFingerTap](begesturetype/onefingertap.md)
  A gesture for a single tap performed with one finger.
- [BEGestureType.oneFingerDoubleTap](begesturetype/onefingerdoubletap.md)
  A gesture for a double tap with a single finger.
- [BEGestureType.oneFingerTripleTap](begesturetype/onefingertripletap.md)
  A gesture for three rapid consecutive taps with one finger.
- [BEGestureType.doubleTap](begesturetype/doubletap.md)
  A gesture for two rapid consecutive taps.
- [BEGestureType.twoFingerSingleTap](begesturetype/twofingersingletap.md)
  A gesture for a single simultaneous tap with two fingers.
### Press and hold gestures
- [BEGestureType.doubleTapAndHold](begesturetype/doubletapandhold.md)
  A gesture for a double tap followed by holding the second tap.
- [BEGestureType.loupe](begesturetype/loupe.md)
  A gesture for touch interactions with the magnifying glass tool.
- [BEGestureType.forceTouch](begesturetype/forcetouch.md)
  A gesture that represents a deep press using 3D Touch or Force Touch.
### Selection and range gestures
- [BEGestureType.twoFingerRangedSelectGesture](begesturetype/twofingerrangedselectgesture.md)
  A gesture to select a range of text with two fingers.
- [BEGestureType.imPhraseBoundaryDrag](begesturetype/imphraseboundarydrag.md)
  A gesture for dragging to adjust input method phrase boundaries.
### Creation of a gesture type
- [init?(rawValue: Int)](begesturetype/init(rawvalue:).md)
  Creates a gesture option of the specified underlying value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class BETextInteraction](betextinteraction.md)
  An interaction you add to a text view to support extended text gestures.
- [protocol BETextInteractionDelegate](betextinteractiondelegate.md)
  A set of methods that informs you about selection changes in text views.
- [protocol BEResponderEditActions](berespondereditactions.md)
  A set of methods that defines extended interactions in browser text views.
- [protocol BEResponderEditActions](berespondereditactions.md)
  A set of methods that defines extended interactions in browser text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/begesturetype)*