# init(location:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new text range at the location you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
convenience init(location: any NSTextLocation)
```

```objc
- (instancetype) initWithLocation:(id<NSTextLocation>) location;
```

## Parameters

- `location`: An [`NSTextLocation`](../nstextlocation.md).

## See Also

### Creating a text range
- [init?(location: any NSTextLocation, end: (any NSTextLocation)?)](./init%28location,end%29.md)
  Creates a new text range with the starting and ending locations you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/init(location:))*