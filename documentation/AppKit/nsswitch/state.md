# state

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current position of the switch.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var state: NSControl.StateValue { get set }
```

```objc
@property NSControlStateValue state;
```

## Discussion

The values [`off`](../nscontrol/statevalue/off.md) and [`on`](../nscontrol/statevalue/on.md) indicate that the switch is in the off or on position. The switch treats any value other than [`off`](../nscontrol/statevalue/off.md) as on.

Setting this property through the [`animator()`](../nsanimatablepropertycontainer/animator%28%29.md) proxy animates the switch to the new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsswitch/state)*