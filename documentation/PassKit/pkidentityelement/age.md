# age

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

An element that represents the user’s age, in years.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class var age: PKIdentityElement { get }
```

```objc
@property (class, nonatomic, readonly) PKIdentityElement * ageElement;
```

## Mentions

- [Requesting identity data from a Wallet pass](../requesting-identity-data-from-a-wallet-pass.md)

## See Also

### Getting an age identity element
- [class func age(atLeast: Int) -> Self](./age%28atleast%29.md)
  Returns an element that represents the user’s age is at least the age you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityelement/age)*