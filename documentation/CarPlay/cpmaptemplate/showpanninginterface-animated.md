# showPanningInterface(animated:)

**Framework**: CarPlay  
**Kind**: method

Shows the panning interface on the map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func showPanningInterface(animated: Bool)
```

#### Discussion

Calling this method while displaying the panning interface has no effect.

While showing the panning interface, the system hides all map buttons. The system doesn’t provide a button to dismiss the panning interface. Instead, you must provide a map button in the navigation bar that the user taps to dismiss the panning interface.

## Parameters

- `animated`: A Boolean value that determines whether to animate the panning interface.

## See Also

- [func dismissPanningInterface(animated: Bool)](cpmaptemplate/dismisspanninginterface(animated:).md)
  Dismisses the panning interface.
- [var isPanningInterfaceVisible: Bool](cpmaptemplate/ispanninginterfacevisible.md)
  A Boolean value that indicates whether the map template is displaying the panning interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/showpanninginterface(animated:))*