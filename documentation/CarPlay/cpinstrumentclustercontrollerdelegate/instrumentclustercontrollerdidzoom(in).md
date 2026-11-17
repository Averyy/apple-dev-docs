# instrumentClusterControllerDidZoom(in:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to increase map magnification by one level.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
optional func instrumentClusterControllerDidZoom(in instrumentClusterController: CPInstrumentClusterController)
```

```objc
- (void) instrumentClusterControllerDidZoomIn:(CPInstrumentClusterController *) instrumentClusterController;
```

## Discussion

Using vehicle controls, someone can change the magnification level of the map you display in the instrument cluster. You define the magnification levels for your content. Each time the system calls this method, increase the magnification of your map’s content by one level. If your map is already at the maximum supported magnification level, don’t magnify it any further.

## Parameters

- `instrumentClusterController`: The controller object associated with your interface.

## See Also

### Handling zoom events
- [func instrumentClusterControllerDidZoomOut(CPInstrumentClusterController)](./instrumentclustercontrollerdidzoomout%28_%29.md)
  Tells the delegate to decrease map magnification by one level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontrollerdelegate/instrumentclustercontrollerdidzoom(in:))*