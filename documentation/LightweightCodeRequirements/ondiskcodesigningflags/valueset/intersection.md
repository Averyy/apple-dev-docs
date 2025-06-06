# intersection(_:)

**Framework**: LightweightCodeRequirements  
**Kind**: method

Returns a new option set with only the elements contained in both this set and the given set.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS ?+
- visionOS ?+
- watchOS ?+

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

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags/valueset/intersection(_:))*