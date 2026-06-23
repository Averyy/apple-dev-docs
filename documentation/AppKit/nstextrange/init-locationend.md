# init(location:end:)

**Framework**: AppKit  
**Kind**: init

Creates a new text range with the starting and ending locations you specify.

**Availability**:
- macOS 12.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/init(location:end:))*