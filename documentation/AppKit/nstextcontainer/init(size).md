# init(size:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a text container with a specified bounding rectangle.

**Availability**:
- macOS 10.11+

## Declaration

```swift
init(size: CGSize)
```

```objc
- (instancetype) initWithSize:(CGSize) size;
```

#### Discussion

The new text container must be added to an [`NSLayoutManager`](../nslayoutmanager.md) object before it can be used. The text container must also have an associated [`NSTextView`](../nstextview.md) object for text to be displayed. This method is the designated initializer for the `NSTextContainer` class.

## Parameters

- `size`: The size of the text container’s bounding rectangle.

## See Also

### Creating a text container
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a text container from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/init(size:))*