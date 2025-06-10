# dismissPanningInterface(animated:)

**Framework**: CarPlay  
**Kind**: method

Dismisses the panning interface.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func dismissPanningInterface(animated: Bool)
```

#### Discussion

When dismissing the panning interface, the system shows the previously hidden map buttons.

## Parameters

- `animated`: A Boolean value that determines whether to animate the dismissal of the panning interface. Set to   to animate the dismissal.

## See Also

- [func showPanningInterface(animated: Bool)](cpmaptemplate/showpanninginterface(animated:).md)
  Shows the panning interface on the map.
- [var isPanningInterfaceVisible: Bool](cpmaptemplate/ispanninginterfacevisible.md)
  A Boolean value that indicates whether the map template is displaying the panning interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/dismisspanninginterface(animated:))*