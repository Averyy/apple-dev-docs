# cellClass

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the `NSBrowserCell` class.

**Availability**:
- macOS

## Declaration

```swift
class var cellClass: AnyClass { get }
```

```objc
@property (class, readonly) Class cellClass;
```

#### Return Value

Always returns the `NSBrowserCell` class (even if the developer has sent a [`setCellClass(_:)`](./setcellclass%28_%29.md) message to a particular instance).

#### Discussion

This method is used by `NSControl` during initialization and is not meant to be used by applications.

## See Also

### Managing Component Types
- [func setCellClass(AnyClass)](./setcellclass%28_%29.md)
  Sets the class of the cell to be used by the matrices in the columns of the browser.
- [var cellPrototype: Any!](./cellprototype.md)
  The prototype `NSCell` for displaying items in the matrices in the columns of the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/cellclass)*