# layoutQueue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The queue on which the framework dispatches layout operations.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var layoutQueue: OperationQueue? { get set }
```

```objc
@property (strong, nullable) NSOperationQueue * layoutQueue;
```

#### Discussion

If non-`nil`, the queue the framework uses for layout operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/layoutqueue)*