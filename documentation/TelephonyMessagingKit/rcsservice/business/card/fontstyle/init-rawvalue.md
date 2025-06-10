# init(rawValue:)

**Framework**: TelephonyMessagingKit  
**Kind**: init

Creates a new option set from the given raw value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(rawValue: Int)
```

#### Discussion

This initializer always succeeds, even if the value passed as `rawValue` exceeds the static properties declared as part of the option set. This example creates an instance of `ShippingOptions` with a raw value beyond the highest element, with a bit mask that effectively contains all the declared static members.

```None
let extraOptions = ShippingOptions(rawValue: 255)
print(extraOptions.isStrictSuperset(of: .all))
// Prints "true"
```

## Parameters

- `rawValue`: The raw value of the option set to create. Each bit   of   potentially represents an element of the option set,   though raw values may include bits that are not defined as distinct   values of the   type.

## See Also

- [let rawValue: Int](rcsservice/business/card/fontstyle/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [RCSService.Business.Card.FontStyle.RawValue](rcsservice/business/card/fontstyle/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/fontstyle/init(rawvalue:))*