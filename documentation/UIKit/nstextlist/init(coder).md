# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly allocated text list item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: An instance of [`NSCoder`](../../Foundation/nscoder.md).

## See Also

### Creating a text list
- [convenience init(markerFormat: NSTextList.MarkerFormat, options: Int)](./init%28markerformat,options%29.md)
  Returns an initialized text list.
- [init(markerFormat: NSTextList.MarkerFormat, options: NSTextList.Options, startingItemNumber: Int)](./init%28markerformat,options,startingitemnumber%29.md)
  Returns a new text list with the format, options, and starting item number you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlist/init(coder:))*