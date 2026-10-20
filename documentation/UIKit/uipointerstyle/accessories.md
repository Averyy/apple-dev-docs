# accessories

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Accessories to display alongside the pointer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var accessories: [UIPointerAccessory] { get set }
```

```objc
@property (nonatomic, copy) NSArray<UIPointerAccessory *> * accessories;
```

#### Discussion

This property supports up to four pointer accessories. The system animates between neighboring or similar accessories.

## See Also

### Specifying pointer accessories
- [class UIPointerAccessory](../uipointeraccessory.md)
  Constants that describe accessories to display alongside the primary pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerstyle/accessories)*