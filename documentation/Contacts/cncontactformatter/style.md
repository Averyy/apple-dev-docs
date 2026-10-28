# style

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The formatting style for the contact name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var style: CNContactFormatterStyle { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic) CNContactFormatterStyle style;
```

*macOS*

```objc
@property (atomic) CNContactFormatterStyle style;
```

## Discussion

The default value for this property is [`CNContactFormatterStyle.fullName`](../cncontactformatterstyle/fullname.md). For more information on formatting styles, see [`CNContactFormatterStyle`](../cncontactformatterstyle.md).

## See Also

### Specifying the formatting style
- [enum CNContactFormatterStyle](../cncontactformatterstyle.md)
  The formatting styles for contact names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter/style)*