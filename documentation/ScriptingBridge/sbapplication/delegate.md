# delegate

**Framework**: Scripting Bridge  
**Kind**: property

The error-handling delegate of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var delegate: (any SBApplicationDelegate)? { get set }
```

#### Discussion

The delegate should implement the [`eventDidFail(_:withError:)`](sbapplicationdelegate/eventdidfail(_:witherror:).md) method of the [`SBApplicationDelegate`](sbapplicationdelegate.md) informal protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/delegate)*