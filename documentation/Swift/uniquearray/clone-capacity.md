# clone(capacity:)

**Framework**: Swift  
**Kind**: method

Copy the contents of this array into a newly allocated unique array instance with the specified capacity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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