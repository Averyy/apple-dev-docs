# didCancelInteracting(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a user interaction with the scrubber has been canceled.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func didCancelInteracting(with scrubber: NSScrubber)
```

```objc
- (void) didCancelInteractingWithScrubber:(NSScrubber *) scrubber;
```

## Parameters

- `scrubber`: The scrubber the user is interacting with.

## See Also

### Tracking user interaction
- [func didBeginInteracting(with: NSScrubber)](./didbegininteracting%28with%29.md)
  Tells the delegate that the user is panning or scrolling the scrubber.
- [func didFinishInteracting(with: NSScrubber)](./didfinishinteracting%28with%29.md)
  Tells the delegate that a pan or scroll interaction with the scrubber has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberdelegate/didcancelinteracting(with:))*