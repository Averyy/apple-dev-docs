# clone(capacity:)

**Framework**: Swift  
**Kind**: method

Copy the contents of this array into a newly allocated unique array instance with the specified capacity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func clone(capacity: Int) -> UniqueArray<Element>
```

#### Discussion

> **Note**: O(`count`)

## Parameters

- `capacity`: The desired capacity of the resulting unique array. `capacity` must be greater than or equal to `count`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/clone(capacity:))*