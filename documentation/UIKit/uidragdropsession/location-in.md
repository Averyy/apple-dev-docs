# location(in:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the geometrical location of the user’s drag activity within the specified view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func location(in view: UIView) -> CGPoint
```

#### Return Value

The location point of the drag activity, in the coordinate system of the specified view.

## Parameters

- `view`: The view whose coordinate system is used to get the location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/location(in:))*