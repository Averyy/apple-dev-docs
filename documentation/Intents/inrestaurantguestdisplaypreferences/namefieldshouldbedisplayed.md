# nameFieldShouldBeDisplayed

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to display the guest’s name should.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var nameFieldShouldBeDisplayed: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) BOOL nameFieldShouldBeDisplayed;
```

*macOS*

```objc
@property (atomic) BOOL nameFieldShouldBeDisplayed;
```

#### Discussion

The default value of this property is [`true`](../../Swift/true.md), which displays the guest’s name.

## See Also

### Specifying Which Fields to Display
- [var phoneNumberFieldShouldBeDisplayed: Bool](./phonenumberfieldshouldbedisplayed.md)
  A Boolean value indicating whether to display the guest’s phone number.
- [var emailAddressFieldShouldBeDisplayed: Bool](./emailaddressfieldshouldbedisplayed.md)
  A Boolean value indicating whether to display the guest’s email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestdisplaypreferences/namefieldshouldbedisplayed)*