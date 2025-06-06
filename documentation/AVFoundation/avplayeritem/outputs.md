# outputs

**Framework**: AVFoundation  
**Kind**: property

An array of outputs associated with the player item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
@MainActor
var outputs: [AVPlayerItemOutput] { get }
```

#### Discussion

This property contains the collection of [`AVPlayerItemOutput`](avplayeritemoutput.md) objects used to transfer media data to the player object.

## See Also

- [func add(AVPlayerItemOutput)](avplayeritem/add(_:)-16ctk.md)
  Adds the specified player item output object to the receiver.
- [func remove(AVPlayerItemOutput)](avplayeritem/remove(_:)-46b1r.md)
  Removes the specified player item output object from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/outputs)*