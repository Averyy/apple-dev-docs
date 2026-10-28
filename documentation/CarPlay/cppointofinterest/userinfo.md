# userInfo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An opaque value for the point of interest.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var userInfo: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id userInfo;
```

## Discussion

Use this property to attach a value that provides additional context for the point of interest. For example, you can attach a model object and reference it in your delegate’s [`pointOfInterestTemplate(_:didSelectPointOfInterest:)`](../cppointofinteresttemplatedelegate/pointofinteresttemplate%28_,didselectpointofinterest%29.md) method when the user selects the point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest/userinfo)*