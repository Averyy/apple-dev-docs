# init(location:end:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new text range with the starting and ending locations you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init?(location: any NSTextLocation, end endLocation: (any NSTextLocation)?)
```

```objc
- (instancetype) initWithLocation:(id<NSTextLocation>) location endLocation:(id<NSTextLocation>) endLocation;
```

#### Discussion

Returns an empty range when `endLocation` is `nil`.

## Parameters

- `location`: The starting location.
- `endLocation`: The ending location, or `nil` for an empty range.

## See Also

### Creating a text range
- [convenience init(location: any NSTextLocation)](./init%28location%29.md)
  Creates a new text range at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/init(location:end:))*