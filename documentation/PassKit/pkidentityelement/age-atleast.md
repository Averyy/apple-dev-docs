# age(atLeast:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns an element that represents the user’s age is at least the age you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class func age(atLeast age: Int) -> Self
```

## Mentions

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)

#### Return Value

An instance with the age you specify if the user’s age is at least the age you specify. If the element is unavailable, this method falls back to a request for [`age`](pkidentityelement/age.md).

## Parameters

- `age`: The age a user must at least be, in years from   to  .

## See Also

- [class var age: PKIdentityElement](pkidentityelement/age.md)
  An element that represents the user’s age, in years.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityelement/age(atleast:))*