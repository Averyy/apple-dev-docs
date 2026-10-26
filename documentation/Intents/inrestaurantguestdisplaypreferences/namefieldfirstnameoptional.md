# nameFieldFirstNameOptional

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the reservation requires the guest’s first name.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var nameFieldFirstNameOptional: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) BOOL nameFieldFirstNameOptional;
```

*macOS*

```objc
@property (atomic) BOOL nameFieldFirstNameOptional;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md), which prevents completion of the reservation if the first name field is empty.

## See Also

### Specifying Required Fields
- [var nameFieldLastNameOptional: Bool](./namefieldlastnameoptional.md)
  A Boolean value indicating whether the reservation requires the guest’s last name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestdisplaypreferences/namefieldfirstnameoptional)*