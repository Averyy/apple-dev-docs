# elements

**Framework**: Game Controller  
**Kind**: property

The input elements of a virtual controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var elements: Set<String> { get set }
```

## Mentions

- [Adding touch controls to games that support game controllers in iOS](adding-touch-controls-to-games-that-support-game-controllers-in-ios.md)

#### Discussion

The possible values you can include in this array are the names of the following constants: [`GCInputButtonA`](gcinputbuttona-8z15w.md), [`GCInputButtonB`](gcinputbuttonb-6z361.md), [`GCInputButtonX`](gcinputbuttonx-32i2z.md), [`GCInputButtonY`](gcinputbuttony-9x9i9.md), [`GCInputDirectionPad`](gcinputdirectionpad-115st.md), [`GCInputLeftThumbstick`](gcinputleftthumbstick-3hlff.md), [`GCInputRightThumbstick`](gcinputrightthumbstick-8469p.md), [`GCInputLeftShoulder`](gcinputleftshoulder-9assr.md), [`GCInputRightShoulder`](gcinputrightshoulder-5lcq1.md), [`GCInputLeftTrigger`](gcinputlefttrigger-80png.md), and [`GCInputRightTrigger`](gcinputrighttrigger-96vtj.md).

> **Note**:  If you include both `GCInputDirectionPad` and `GCInputLeftThumbstick` in the array, the virtual controller contains only the left thumb stick, not the input direction pad.

 If you include both `GCInputDirectionPad` and `GCInputLeftThumbstick` in the array, the virtual controller contains only the left thumb stick, not the input direction pad.

For example, configure a virtual controller with a left thumb stick, right thumb stick, A button, and B button.

```swift
virtualConfiguration.elements = [GCInputLeftThumbstick,GCInputRightThumbstick,GCInputButtonA,GCInputButtonB]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/configuration/elements)*