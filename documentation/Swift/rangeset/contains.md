# contains(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the given value is contained by the ranges in the range set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func contains(_ value: Bound) -> Bool
```

#### Return Value

`true` if `value` is contained by a range in the range set; otherwise, `false`.

#### Discussion

> **Note**: O(log ), where  is the number of ranges in the range set.

O(log ), where  is the number of ranges in the range set.

## Parameters

- `value`: The value to look for in the range set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/contains(_:))*