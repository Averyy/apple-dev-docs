# prefersHorizontalTextLayout

**Framework**: Accessibility  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the system setting to prefer horizontal text for languages that support both vertical and horizontal text layout is on.

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
static var prefersHorizontalTextLayout: Bool { get }
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the system setting for Prefer Horizontal Text is on; otherwise, [`false`](../../Swift/false.md).

## See Also

### Customizing vertical text layout
- [Horizontal text](../horizontal-text.md)
  Lay out vertical text horizontally in your app when people turn on the Prefer Horizontal Text setting.
- [static var prefersHorizontalTextLayoutDidChangeNotification: Notification.Name](./prefershorizontaltextlayoutdidchangenotification.md)
  A notification that posts when the system setting to prefer horizontal text for languages that support both vertical and horizontal text layout changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/prefershorizontaltextlayout)*