# didBeginInteracting(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user is panning or scrolling the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func didBeginInteracting(with scrubber: NSScrubber)
```

```objc
- (void) didBeginInteractingWithScrubber:(NSScrubber *) scrubber;
```

## Parameters

- `scrubber`: The scrubber the user is interacting with.

## See Also

### Tracking user interaction
- [func didFinishInteracting(with: NSScrubber)](./didfinishinteracting%28with%29.md)
  Tells the delegate that a pan or scroll interaction with the scrubber has ended.
- [func didCancelInteracting(with: NSScrubber)](./didcancelinteracting%28with%29.md)
  Tells the delegate that a user interaction with the scrubber has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberdelegate/didbegininteracting(with:))*