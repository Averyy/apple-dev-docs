# phoneNumberFieldShouldBeDisplayed

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to display the guest’s phone number.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var phoneNumberFieldShouldBeDisplayed: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) BOOL phoneNumberFieldShouldBeDisplayed;
```

*macOS*

```objc
@property (atomic) BOOL phoneNumberFieldShouldBeDisplayed;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md), which displays the guest’s phone number.

## See Also

### Specifying Which Fields to Display
- [var nameFieldShouldBeDisplayed: Bool](./namefieldshouldbedisplayed.md)
  A Boolean value indicating whether to display the guest’s name should.
- [var emailAddressFieldShouldBeDisplayed: Bool](./emailaddressfieldshouldbedisplayed.md)
  A Boolean value indicating whether to display the guest’s email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestdisplaypreferences/phonenumberfieldshouldbedisplayed)*