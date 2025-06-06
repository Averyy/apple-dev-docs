# isAnimating()

**Framework**: Messages  
**Kind**: method

Returns a Boolean value that indicates whether the sticker is animating.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func isAnimating() -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the sticker is animating; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var animationDuration: TimeInterval](msstickerview/animationduration.md)
  The amount of time it takes to complete the sticker’s animation.
- [func startAnimating()](msstickerview/startanimating.md)
  Starts the sticker’s animation, beginning with the first frame.
- [func stopAnimating()](msstickerview/stopanimating.md)
  Stops the sticker’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerview/isanimating())*