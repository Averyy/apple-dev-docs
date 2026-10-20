# shouldUpdateFocus(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
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
func shouldUpdateFocus(in context: UIFocusUpdateContext) -> Bool
```

```objc
- (BOOL) shouldUpdateFocusInContext:(UIFocusUpdateContext *) context;
```

#### Return Value

[`true`](../../Swift/true.md) to allow the focus update; otherwise, [`false`](../../Swift/false.md).

#### Discussion

When a focus update is about to occur, the focus engine calls this method on all focus environments that contain either the previously focused view, the next focused view, or both, in ascending order. If any environment returns [`false`](../../Swift/false.md), the update is cancelled. Override this method to prevent the focus from moving to or from certain areas of the screen.

## Parameters

- `context`: An instance of [`UIFocusUpdateContext`](../uifocusupdatecontext.md) class, containing metadata for the focus related update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/shouldupdatefocus(in:))*