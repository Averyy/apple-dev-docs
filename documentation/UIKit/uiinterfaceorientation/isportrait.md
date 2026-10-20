# isPortrait

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user interface is currently presented in a portrait orientation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
var isPortrait: Bool { get }
```

```c
static BOOL UIInterfaceOrientationIsPortrait(UIInterfaceOrientation orientation);
```

#### Discussion

The interface orientation can be different than the device orientation. You typically call this function in your view controller code to check the current orientation.

## See Also

### Interface orientation
- [var isLandscape: Bool](./islandscape.md)
  A Boolean value that indicates whether the user interface is currently presented in a landscape orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinterfaceorientation/isportrait)*