# contains(_:)

**Framework**: App Intents  
**Kind**: method

Returns a Boolean value that indicates whether a given element is a member of the option set.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func contains(_ member: Self) -> Bool
```

#### Return Value

`true` if the option set contains `member`; otherwise, `false`.

#### Discussion

This example uses the `contains(_:)` method to check whether next-day shipping is in the `availableOptions` instance.

```swift
let availableOptions = ShippingOptions.express
if availableOptions.contains(.nextDay) {
    print("Next day shipping available")
}
// Prints "Next day shipping available"
```

## Parameters

- `member`: The element to look for in the option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/confirmationconditions/contains(_:))*