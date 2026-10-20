# dismiss(in:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Dismisses an App Store overlay.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func dismiss(in scene: UIWindowScene)
```

```objc
+ (void) dismissOverlayInScene:(UIWindowScene *) scene;
```

## Parameters

- `scene`: The window scene used to display the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/dismiss(in:))*