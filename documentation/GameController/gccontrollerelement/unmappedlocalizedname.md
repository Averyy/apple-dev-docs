# unmappedLocalizedName

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The element’s localized name, not the remapped name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var unmappedLocalizedName: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * unmappedLocalizedName;
```

## Discussion

To present the element that a user wants to remap in your interface, use this property to get the original name. Otherwise, use the [`localizedName`](./localizedname.md) property to get the possibly remapped name.

## See Also

### Getting a localized name
- [var localizedName: String?](./localizedname.md)
  The localized name for the element or the remapped element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/unmappedlocalizedname)*