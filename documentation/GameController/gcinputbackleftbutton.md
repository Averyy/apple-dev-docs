# GCInputBackLeftButton

**Framework**: Game Controller  
**Kind**: func  
**Role**: Function

Returns the name of the back left button at the specified location.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```c
extern GCInputButtonNameGCInputBackLeftButton(NSInteger position);
```

## Return Value

The name of the back left button.

## Parameters

- `position`: The relative position of the button to the other back left button. Pass `0` for the button nearest to the natural rest position of the person’s finger. Pass `1` for an additional button that requires the person to move their fingers to press if it exists.

## See Also

### Additional back button names
- [GCInputBackRightButton](./gcinputbackrightbutton.md)
  Returns the name of the back right button at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcinputbackleftbutton)*