# customView(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a new calendar view decoration with a custom view, using your view provider.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class func customView(_ customViewProvider: @escaping () -> UIView) -> Self
```

```objc
+ (instancetype) decorationWithCustomViewProvider:(UIView * (^)()) customViewProvider;
```

## Return Value

A calendar view decoration.

## Discussion

Create and return a decoration view for the calendar view in your `customViewProvider` block. The calendar view will clip the decoration view to its parent’s bounds. The decoration view may not have any interactions.

## Parameters

- `customViewProvider`: A block of code that creates and returns a calendar view decoration.

## See Also

### Creating a Custom Decoration View
- [- initWithCustomViewProvider:](../../uicalendarviewdecoration/initwithcustomviewprovider_.md)
  Creates a new calendar view decoration with a custom view, using your view provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/decoration/customview(_:))*