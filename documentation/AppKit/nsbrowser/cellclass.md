# cellClass

**Framework**: AppKit  
**Kind**: property

Returns the `NSBrowserCell` class.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var cellClass: AnyClass { get }
```

#### Return Value

Always returns the `NSBrowserCell` class (even if the developer has sent a [`setCellClass(_:)`](nsbrowser/setcellclass(_:).md) message to a particular instance).

#### Discussion

This method is used by `NSControl` during initialization and is not meant to be used by applications.

## See Also

- [func setCellClass(AnyClass)](nsbrowser/setcellclass(_:).md)
  Sets the class of the cell to be used by the matrices in the columns of the browser.
- [var cellPrototype: Any!](nsbrowser/cellprototype.md)
  The prototype `NSCell` for displaying items in the matrices in the columns of the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/cellclass)*