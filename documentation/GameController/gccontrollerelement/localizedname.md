# localizedName

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The localized name for the element or the remapped element.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var localizedName: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * localizedName;
```

## Discussion

If the user remaps this element, this property is the remapped localized name.

## See Also

### Getting a localized name
- [var unmappedLocalizedName: String?](./unmappedlocalizedname.md)
  The element’s localized name, not the remapped name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/localizedname)*