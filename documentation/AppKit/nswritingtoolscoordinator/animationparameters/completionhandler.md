# completionHandler

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A custom block to run when the system animations finish.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var completionHandler: (() -> Void)? { get set }
```

```objc
@property (copy, nullable) void (^completionHandler)();
```

#### Discussion

Set this property to a block that you want the system to run when any animations finish. The block you provide must have no return value and no parameters. The system executes this block once when the current animation finish.

## See Also

### Creating custom animations
- [var progressHandler: ((Float) -> Void)?](./progresshandler.md)
  A custom block that runs at the same time as the system animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/animationparameters/completionhandler)*