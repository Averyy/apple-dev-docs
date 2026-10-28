# phoneNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The driver’s phone number.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var phoneNumber: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * phoneNumber;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * phoneNumber;
```

## Discussion

When displaying information about the driver, the system displays the provided string as-is and does not try to format it. You are responsible for formatting the phone number appropriately for the user’s locale.

## See Also

### Getting the Driver Information
- [var rating: String?](./rating.md)
  The driver’s current rating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridedriver/phonenumber)*