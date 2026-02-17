# intersection(_:)

**Framework**: Swift  
**Kind**: method

Returns a new option set with only the elements contained in both this set and the given set.

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
func intersection(_ other: Self) -> Self
```

#### Return Value

A new option set with only the elements contained in both this set and `other`.

#### Discussion

This example uses the `intersection(_:)` method to limit the available shipping options to what can be used with a PO Box destination.

```swift
// Can only ship standard or priority to PO Boxes
let poboxShipping: ShippingOptions = [.standard, .priority]
let memberShipping: ShippingOptions =
        [.standard, .priority, .secondDay]

let availableOptions = memberShipping.intersection(poboxShipping)
print(availableOptions.contains(.priority))
// Prints "true"
print(availableOptions.contains(.secondDay))
// Prints "false"
```

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clocktraits/intersection(_:))*