# init(markerFormat:options:startingItemNumber:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns a new text list with the format, options, and starting item number you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(markerFormat: NSTextList.MarkerFormat, options: NSTextList.Options = [], startingItemNumber: Int)
```

```objc
- (instancetype) initWithMarkerFormat:(NSTextListMarkerFormat) markerFormat options:(NSTextListOptions) options startingItemNumber:(NSInteger) startingItemNumber;
```

## Parameters

- `markerFormat`: One of the possible [`NSTextList.MarkerFormat`](./markerformat-swift.struct.md) formats.
- `options`: One or more of the possible [`NSTextList.Options`](./options.md) options.
- `startingItemNumber`: An integer that represents the stating item number.

## See Also

### Creating a text list
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes and returns a newly allocated text list item.
- [convenience init(markerFormat: NSTextList.MarkerFormat, options: Int)](./init%28markerformat,options%29.md)
  Returns an initialized text list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlist/init(markerformat:options:startingitemnumber:))*