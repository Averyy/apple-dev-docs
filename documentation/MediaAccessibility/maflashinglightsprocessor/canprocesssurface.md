# canProcessSurface(_:)

**Framework**: Media Accessibility  
**Kind**: method

Returns a Boolean value that indicates whether the flashing lights processor can process the content in the surface for sequences of flashing lights.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func canProcessSurface(_ surface: IOSurfaceRef) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the processor can process the content in the surface for flashing lights. [`false`](https://developer.apple.com/documentation/swift/false) if the processor can’t process the surface, which can occur for unsupported hardware or unsupported color spaces.

## Parameters

- `surface`: The   to process for flashing lights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor/canprocesssurface(_:))*