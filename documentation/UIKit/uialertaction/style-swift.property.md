# style

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style that applies to the action’s button.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var style: UIAlertAction.Style { get }
```

```objc
@property (nonatomic, readonly) UIAlertActionStyle style;
```

## Discussion

This property is set to the value you specified in the [`init(title:style:handler:)`](./init%28title,style,handler%29.md) method.

## See Also

### Getting the action’s attributes
- [var title: String?](./title.md)
  The title of the action’s button.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the action is currently enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertaction/style-swift.property)*