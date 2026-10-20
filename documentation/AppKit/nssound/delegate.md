# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The sound’s delegate.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSSoundDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSSoundDelegate> delegate;
```

## See Also

### Detecting When a Sound Finishes Playing
- [protocol NSSoundDelegate](../nssounddelegate.md)
  A set of optional methods implemented by delegates of [`NSSound`](../nssound.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/delegate)*