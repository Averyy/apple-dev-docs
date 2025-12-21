# animatedImagesEnabled

**Framework**: Accessibility  
**Kind**: property

A Boolean value that indicates whether the system setting for playing animated images is on.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static var animatedImagesEnabled: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the system setting for Animated Images is on; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [Animated images](animated-images.md)
  Pause animations in animated images in your app when people turn off the Animated Images setting.
- [static var animatedImagesEnabledDidChangeNotification: Notification.Name](accessibilitysettings/animatedimagesenableddidchangenotification.md)
  A notification that posts when the system setting for playing animated images changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/animatedimagesenabled)*