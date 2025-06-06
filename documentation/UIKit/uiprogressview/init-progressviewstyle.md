# init(progressViewStyle:)

**Framework**: UIKit  
**Kind**: init

Creates a progress view with the specified style.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(progressViewStyle style: UIProgressView.Style)
```

#### Return Value

An initialized [`UIProgressView`](uiprogressview.md) object.

#### Discussion

[`UIProgressView`](uiprogressview.md) sets the height of the returned view according to the specified `style`. You can set and retrieve the style of a progress view through the [`progressViewStyle`](uiprogressview/progressviewstyle.md) property.

## Parameters

- `style`: A constant that specifies the style of the object to be created. See   for descriptions of the style constants.

## See Also

- [init(frame: CGRect)](uiprogressview/init(frame:).md)
  Creates a progress view with the specified frame rectangle.
- [init?(coder: NSCoder)](uiprogressview/init(coder:).md)
  Creates a progress view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/init(progressviewstyle:))*