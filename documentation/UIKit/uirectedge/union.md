# union(_:)

**Framework**: UIKit  
**Kind**: method

Returns a new option set of the elements contained in this set, in the given set, or in both.

**Availability**:
- iOS ?+
- iPadOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func union(_ other: Self) -> Self
```

#### Return Value

A new option set made up of the elements contained in this set, in `other`, or in both.

#### Discussion

This example uses the `union(_:)` method to add two more shipping options to the default set.

```None
let defaultShipping = ShippingOptions.standard
let memberShipping = defaultShipping.union([.secondDay, .priority])
print(memberShipping.contains(.priority))
// Prints "true"
```

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectedge/union(_:))*