# init(coder:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a view using from data in the specified coder object.

**Availability**:
- macOS

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Return Value

An initialized view or `nil` if AppKit couldn’t create the object.

## Parameters

- `coder`: The coder object that contains the view’s configuration details.

## See Also

### Creating a view object
- [init(frame: NSRect)](./init%28frame%29.md)
  Initializes and returns a newly allocated `NSView` object with a specified frame rectangle.
- [func prepareForReuse()](./prepareforreuse%28%29.md)
  Restores the view to an initial state so that it can be reused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/init(coder:))*