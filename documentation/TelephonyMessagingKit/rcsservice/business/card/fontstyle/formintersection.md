# formIntersection(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Removes all elements of this option set that are not also present in the given set.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
mutating func formIntersection(_ other: Self)
```

#### Discussion

This method is implemented as a `&` (bitwise AND) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/fontstyle/formintersection(_:))*