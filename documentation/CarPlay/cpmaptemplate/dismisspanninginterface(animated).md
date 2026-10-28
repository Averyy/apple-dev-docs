# dismissPanningInterface(animated:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Dismisses the panning interface.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func dismissPanningInterface(animated: Bool)
```

```objc
- (void) dismissPanningInterfaceAnimated:(BOOL) animated;
```

## Discussion

When dismissing the panning interface, the system shows the previously hidden map buttons.

## Parameters

- `animated`: A Boolean value that determines whether to animate the dismissal of the panning interface. Set to [`true`](../../Swift/true.md) to animate the dismissal.

## See Also

### Panning the Map
- [func showPanningInterface(animated: Bool)](./showpanninginterface%28animated%29.md)
  Shows the panning interface on the map.
- [var isPanningInterfaceVisible: Bool](./ispanninginterfacevisible.md)
  A Boolean value that indicates whether the map template is displaying the panning interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/dismisspanninginterface(animated:))*