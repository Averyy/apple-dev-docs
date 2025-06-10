# intersection(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Returns a new option set with only the elements contained in both this set and the given set.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
func intersection(_ other: Self) -> Self
```

#### Return Value

A new option set with only the elements contained in both this set and `other`.

#### Discussion

This example uses the `intersection(_:)` method to limit the available shipping options to what can be used with a PO Box destination.

```None
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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/fontstyle/intersection(_:))*