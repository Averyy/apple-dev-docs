# nameFieldLastNameOptional

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the reservation requires the guest’s last name.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var nameFieldLastNameOptional: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) BOOL nameFieldLastNameOptional;
```

*macOS*

```objc
@property (atomic) BOOL nameFieldLastNameOptional;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md), which prevents completion of the reservation if the last name field is empty.

## See Also

### Specifying Required Fields
- [var nameFieldFirstNameOptional: Bool](./namefieldfirstnameoptional.md)
  A Boolean value indicating whether the reservation requires the guest’s first name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestdisplaypreferences/namefieldlastnameoptional)*