# init(coder:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly allocated text list item.

**Availability**:
- macOS 10.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlist/init(coder:))*