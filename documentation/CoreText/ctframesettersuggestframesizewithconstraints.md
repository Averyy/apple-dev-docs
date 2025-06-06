# CTFramesetterSuggestFrameSizeWithConstraints(_:_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Determines the frame size needed for a string range.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFramesetterSuggestFrameSizeWithConstraints(_ framesetter: CTFramesetter, _ stringRange: CFRange, _ frameAttributes: CFDictionary?, _ constraints: CGSize, _ fitRange: UnsafeMutablePointer<CFRange>?) -> CGSize
```

#### Return Value

The actual dimensions for the given string range and constraints.

#### Discussion

This function can be used to determine how much space is needed to display a string, optionally by constraining the space along either dimension.

## Parameters

- `framesetter`: The framesetter used for measuring the frame size.
- `stringRange`: The string range to which the frame size applies. The string range is a range over the string used to create the framesetter. If the length portion of the range is set to  , then the framesetter continues to add lines until it runs out of text or space.
- `frameAttributes`: Additional attributes that control the frame filling process, or   if there are no such attributes.
- `constraints`: The width and height to which the frame size is constrained. A value of   for either dimension indicates that it should be treated as unconstrained.
- `fitRange`: On return, contains the range of the string that actually fit in the constrained size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframesettersuggestframesizewithconstraints(_:_:_:_:_:))*