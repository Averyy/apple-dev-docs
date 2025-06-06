# init(rawValue:)

**Framework**: RealityKit  
**Kind**: init

Creates a new option set from the given raw value.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
init(rawValue: UInt32)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct/init(rawvalue:))*