# carTraitCollection

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The trait collection of the vehicle’s primary screen.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var carTraitCollection: UITraitCollection { get }
```

```objc
@property (nonatomic, strong, readonly) UITraitCollection * carTraitCollection;
```

## Discussion

Use this trait collection to derive metrics for the content you display in your CarPlay interface. For example, create or select images at the display scale you get from this trait collection, and not from the display scale from the person’s iPhone.

## See Also

### Configuring interface-related details
- [var prefersDarkUserInterfaceStyle: Bool](./prefersdarkuserinterfacestyle.md)
  A Boolean value that indicates whether you prefer Dark Mode for your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/cartraitcollection)*