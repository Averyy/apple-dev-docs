# init(frame:inputViewStyle:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns an input view using the specified style information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(frame: CGRect, inputViewStyle: UIInputView.Style)
```

#### Return Value

An initialized view object or `nil` if the view could not be initialized.

#### Discussion

This method is the designated initializer for the view and must be called by your subclass at initialization time.

## Parameters

- `frame`: The frame rectangle for the view, measured in points. The origin of the frame is relative to the superview in which you plan to add it.
- `inputViewStyle`: The style to use when altering the appearance of the view and its subviews. For a list of possible values, see 

## See Also

- [init?(coder: NSCoder)](uiinputview/init(coder:).md)
  Creates an input view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputview/init(frame:inputviewstyle:))*