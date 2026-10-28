# outputs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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
nonisolated
var outputs: [AVPlayerItemOutput] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVPlayerItemOutput *> * outputs;
```

## Discussion

This property contains the collection of [`AVPlayerItemOutput`](../avplayeritemoutput.md) objects used to transfer media data to the player object.

## See Also

### Managing player item outputs
- [func add(AVPlayerItemOutput)](./add%28_%29-16ctk.md)
  Adds the specified player item output object to the receiver.
- [func remove(AVPlayerItemOutput)](./remove%28_%29-46b1r.md)
  Removes the specified player item output object from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/outputs)*