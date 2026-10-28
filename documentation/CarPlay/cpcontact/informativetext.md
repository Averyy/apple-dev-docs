# informativeText

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Additional text that the template displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var informativeText: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * informativeText;
```

## Discussion

Use this property to display additional information about the contact. For example, their address or a short bio.

The default value is [`nil`](../../ObjectiveC/nil-227m0.md).

## See Also

### Configuring the Contact’s Attributes
- [var image: UIImage](./image.md)
  The contact’s image.
- [var name: String](./name.md)
  The contact’s name.
- [var subtitle: String?](./subtitle.md)
  A subtitle that the template displays in addition to the contact’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontact/informativetext)*