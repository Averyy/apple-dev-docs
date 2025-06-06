# pointOfInterestTemplate(_:didSelectPointOfInterest:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate when the user selects a point of interest.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func pointOfInterestTemplate(_ pointOfInterestTemplate: CPPointOfInterestTemplate, didSelectPointOfInterest pointOfInterest: CPPointOfInterest)
```

#### Discussion

CarPlay calls this method whenever the user selects a point of interest from the template’s map. The template displays a detail card for the selection, which contains secondary information and optional actions the user can perform.

Use the [`userInfo`](cppointofinterest/userinfo.md) property to attach a value that provides additional context for the point of interest. You can then reference that value in your implementation of this method.

## Parameters

- `pointOfInterestTemplate`: The template that displays the map that contains the points of interest.
- `pointOfInterest`: The point of interest that the user selects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplatedelegate/pointofinteresttemplate(_:didselectpointofinterest:))*