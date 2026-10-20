# init(location:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new text range at the location you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextrange/init(location:))*