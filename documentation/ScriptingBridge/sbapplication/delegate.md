# delegate

**Framework**: Scripting Bridge  
**Kind**: property  
**Role**: Instance Property

The error-handling delegate of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var delegate: (any SBApplicationDelegate)? { get set }
```

```objc
@property (strong, nullable) id<SBApplicationDelegate> delegate;
```

## Discussion

The delegate should implement the [`eventDidFail(_:withError:)`](../sbapplicationdelegate/eventdidfail%28_,witherror%29.md) method of the [`SBApplicationDelegate`](../sbapplicationdelegate.md) informal protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/delegate)*