# init(coder:)

**Framework**: AppKit  
**Kind**: init

Initializes a view using from data in the specified coder object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init?(coder: NSCoder)
```

#### Return Value

An initialized view or `nil` if AppKit couldn’t create the object.

## Parameters

- `coder`: The coder object that contains the view’s configuration details.

## See Also

- [init(frame: NSRect)](nsview/init(frame:).md)
  Initializes and returns a newly allocated `NSView` object with a specified frame rectangle.
- [func prepareForReuse()](nsview/prepareforreuse.md)
  Restores the view to an initial state so that it can be reused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/init(coder:))*