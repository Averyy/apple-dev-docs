# pointOfInterestDelegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The object that serves as the template’s delegate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
weak var pointOfInterestDelegate: (any CPPointOfInterestTemplateDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CPPointOfInterestTemplateDelegate> pointOfInterestDelegate;
```

## See Also

### Handling Template Events
- [protocol CPPointOfInterestTemplateDelegate](../cppointofinteresttemplatedelegate.md)
  The methods to handle a Point of Interest template’s events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate/pointofinterestdelegate)*