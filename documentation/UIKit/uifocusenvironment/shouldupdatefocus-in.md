# shouldUpdateFocus(in:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value indicating whether the focus engine should allow the focus update described by the specified context to occur.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func shouldUpdateFocus(in context: UIFocusUpdateContext) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to allow the focus update; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

When a focus update is about to occur, the focus engine calls this method on all focus environments that contain either the previously focused view, the next focused view, or both, in ascending order. If any environment returns [`false`](https://developer.apple.com/documentation/swift/false), the update is cancelled. Override this method to prevent the focus from moving to or from certain areas of the screen.

## Parameters

- `context`: An instance of   class, containing metadata for the focus related update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/shouldupdatefocus(in:))*