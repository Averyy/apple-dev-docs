# subtitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A subtitle that the template displays in addition to the contact’s name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var subtitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * subtitle;
```

#### Discussion

Use this property to display secondary information about the contact. For example, their job title or email address.

The default value is [`nil`](../../ObjectiveC/nil-227m0.md).

## See Also

### Configuring the Contact’s Attributes
- [var image: UIImage](./image.md)
  The contact’s image.
- [var name: String](./name.md)
  The contact’s name.
- [var informativeText: String?](./informativetext.md)
  Additional text that the template displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontact/subtitle)*