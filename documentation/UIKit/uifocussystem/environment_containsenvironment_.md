# environment:containsEnvironment:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether one focus environment is contained by another.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
+ (BOOL) environment:(id<UIFocusEnvironment>) environment containsEnvironment:(id<UIFocusEnvironment>) otherEnvironment;
```

## Return Value

[`true`](../../Swift/true.md) if `environment` is an ancestor of `otherEnvironment`, or [`false`](../../Swift/false.md) if it is not.

## Discussion

Use this method to determine if the two environments are related. For example, you might specify a [`UIWindow`](../uiwindow.md) object for `environment` and a [`UIView`](../uiview.md) object for `otherEnvironment` to determine if the view is displayed by that window.

## Parameters

- `environment`: The object whose children you want to check.
- `otherEnvironment`: The target object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussystem/environment:containsenvironment:)*