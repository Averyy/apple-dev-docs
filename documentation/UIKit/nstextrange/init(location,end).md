# init(location:end:)

**Framework**: UIKit  
**Kind**: init

Creates a new text range with the starting and ending locations you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init?(location: any NSTextLocation, end endLocation: (any NSTextLocation)?)
```

#### Discussion

Returns an empty range when `endLocation` is `nil`.

## Parameters

- `location`: The starting location.
- `endLocation`: The ending location, or `nil` for an empty range.

## See Also

- [convenience init(location: any NSTextLocation)](nstextrange/init(location:).md)
  Creates a new text range at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextrange/init(location:end:))*