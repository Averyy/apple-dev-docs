# contains(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a Boolean value that indicates whether a given element is a member of the option set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
func contains(_ member: Self) -> Bool
```

#### Return Value

`true` if the option set contains `member`; otherwise, `false`.

#### Discussion

This example uses the `contains(_:)` method to check whether next-day shipping is in the `availableOptions` instance.

```None
let availableOptions = ShippingOptions.express
if availableOptions.contains(.nextDay) {
    print("Next day shipping available")
}
// Prints "Next day shipping available"
```

## Parameters

- `member`: The element to look for in the option set.

## See Also

- [var isEmpty: Bool](arview/renderoptions-swift.struct/isempty.md)
  A Boolean value that indicates whether the set has no elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/contains(_:))*