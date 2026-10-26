# rating

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The driver’s current rating.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var rating: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * rating;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * rating;
```

#### Discussion

Siri displays the string you provide when displaying the status of a ride request.

## See Also

### Getting the Driver Information
- [var phoneNumber: String?](./phonenumber.md)
  The driver’s phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridedriver/rating)*