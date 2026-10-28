# cancel()

**Framework**: Social  
**Kind**: method  
**Role**: Instance Method

Starts the animated dismissal of the compose view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

## Discussion

When the cancel animation finishes, this method calls [`didSelectCancel()`](./didselectcancel%28%29.md). A subclass shouldn’t need to override `cancel`. In rare cases a subclass may call `cancel`, such as in response to a catastrophic failure during user interaction with the compose view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/cancel())*