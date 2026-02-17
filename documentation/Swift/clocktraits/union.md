# union(_:)

**Framework**: Swift  
**Kind**: method

Returns a new option set of the elements contained in this set, in the given set, or in both.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func union(_ other: Self) -> Self
```

#### Return Value

A new option set made up of the elements contained in this set, in `other`, or in both.

#### Discussion

This example uses the `union(_:)` method to add two more shipping options to the default set.

```swift
let defaultShipping = ShippingOptions.standard
let memberShipping = defaultShipping.union([.secondDay, .priority])
print(memberShipping.contains(.priority))
// Prints "true"
```

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clocktraits/union(_:))*