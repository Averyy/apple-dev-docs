# updateConfiguration(forElement:configuration:)

**Framework**: Game Controller  
**Kind**: method

Changes the configuration for one of the virtual controller’s input elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func updateConfiguration(forElement element: String, configuration config: (GCVirtualController.ElementConfiguration) -> GCVirtualController.ElementConfiguration)
```

## Mentions

- [Adding touch controls to games that support game controllers in iOS](adding-touch-controls-to-games-that-support-game-controllers-in-ios.md)

## Parameters

- `element`: The element whose configuration you want to change. For the possible values of this parameter, see the   property.
- `config`: The new configuration for the element.

## See Also

- [GCVirtualController.ElementConfiguration](gcvirtualcontroller/elementconfiguration.md)
  The properties of a virtual controller’s element that you can customize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/updateconfiguration(forelement:configuration:))*