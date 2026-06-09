# containerConcentric(_:)

**Framework**: AppKit  
**Kind**: method

A dynamic corner radius calculated based on the view’s container shape and limited to the provided minimum radius.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
class func containerConcentric(_ minimumRadius: CGFloat) -> NSViewCornerRadius
```

## Parameters

- `minimumRadius`: Corner radius that’s applied when a corner of the view’s container is smaller than the specified radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcornerradius/containerconcentric(_:))*