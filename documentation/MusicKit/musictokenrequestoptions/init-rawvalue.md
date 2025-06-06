# init(rawValue:)

**Framework**: MusicKit  
**Kind**: init

Creates a new option set from the given raw value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(rawValue: Int)
```

#### Discussion

This initializer always succeeds, even if the value passed as `rawValue` exceeds the static properties declared as part of the option set. This example creates an instance of `ShippingOptions` with a raw value beyond the highest element, with a bit mask that effectively contains all the declared static members.

```swift
let extraOptions = ShippingOptions(rawValue: 255)
print(extraOptions.isStrictSuperset(of: .all))
// Prints "true"
```

## Parameters

- `rawValue`: The raw value of the option set to create. Each bit   of   potentially represents an element of the option set,   though raw values may include bits that are not defined as distinct   values of the   type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musictokenrequestoptions/init(rawvalue:))*