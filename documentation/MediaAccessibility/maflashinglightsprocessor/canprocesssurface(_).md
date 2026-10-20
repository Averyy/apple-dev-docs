# canProcessSurface(_:)

**Framework**: Media Accessibility  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) canProcessSurface:(IOSurfaceRef) surface;
```

#### Return Value

[`true`](../../Swift/true.md) if the processor can process the content in the surface for flashing lights. [`false`](../../Swift/false.md) if the processor can’t process the surface, which can occur for unsupported hardware or unsupported color spaces.

## Parameters

- `surface`: The [`IOSurfaceRef`](../../IOSurface/iosurfaceref.md) to process for flashing lights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor/canprocesssurface(_:))*