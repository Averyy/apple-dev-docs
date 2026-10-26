# emailAddressFieldShouldBeDisplayed

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to display the guest’s email address.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var emailAddressFieldShouldBeDisplayed: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) BOOL emailAddressFieldShouldBeDisplayed;
```

*macOS*

```objc
@property (atomic) BOOL emailAddressFieldShouldBeDisplayed;
```

#### Discussion

The default value of this property is [`true`](../../Swift/true.md), which displays the guest’s email address.

## See Also

### Specifying Which Fields to Display
- [var nameFieldShouldBeDisplayed: Bool](./namefieldshouldbedisplayed.md)
  A Boolean value indicating whether to display the guest’s name should.
- [var phoneNumberFieldShouldBeDisplayed: Bool](./phonenumberfieldshouldbedisplayed.md)
  A Boolean value indicating whether to display the guest’s phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestdisplaypreferences/emailaddressfieldshouldbedisplayed)*