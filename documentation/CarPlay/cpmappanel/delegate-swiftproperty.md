# delegate

**Framework**: CarPlay  
**Kind**: property

The app-specific object that the system notifies when it hides and shows the panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
weak var delegate: (any CPMapPanel.Delegate)? { get set }
```

#### Discussion

Specify a custom object that adopts the [`CPMapPanel.Delegate`](cpmappanel/delegate-swift.protocol.md) protocol if you want to know when the map panel appears or disappears from your CarPlay interface. The system maintains a weak reference to the object you provide, so keep a reference to the object in your own code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanel/delegate-swift.property)*