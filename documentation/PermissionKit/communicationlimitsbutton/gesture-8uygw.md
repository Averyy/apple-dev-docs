# gesture(_:)

**Framework**: PermissionKit  
**Kind**: method

Attaches an `NSGestureRecognizerRepresentable` to the view.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func gesture(_ representable: some NSGestureRecognizerRepresentable) -> some View
```

#### Return Value

A view with an `NSGestureRecognizerRepresentable` attached.

## Parameters

- `representable`: The    that creates and manages a gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/gesture(_:)-8uygw)*