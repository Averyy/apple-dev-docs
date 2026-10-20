# showPanningInterface(animated:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Shows the panning interface on the map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func showPanningInterface(animated: Bool)
```

```objc
- (void) showPanningInterfaceAnimated:(BOOL) animated;
```

#### Discussion

Calling this method while displaying the panning interface has no effect.

While showing the panning interface, the system hides all map buttons. The system doesn’t provide a button to dismiss the panning interface. Instead, you must provide a map button in the navigation bar that the user taps to dismiss the panning interface.

## Parameters

- `animated`: A Boolean value that determines whether to animate the panning interface.

## See Also

### Panning the Map
- [func dismissPanningInterface(animated: Bool)](./dismisspanninginterface%28animated%29.md)
  Dismisses the panning interface.
- [var isPanningInterfaceVisible: Bool](./ispanninginterfacevisible.md)
  A Boolean value that indicates whether the map template is displaying the panning interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/showpanninginterface(animated:))*