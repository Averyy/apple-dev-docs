# cellPrototype

**Framework**: AppKit  
**Kind**: property

The prototype `NSCell` for displaying items in the matrices in the columns of the browser.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var cellPrototype: Any! { get set }
```

#### Discussion

The prototype `NSCell` instance is copied to display items in the matrices of the browser.

## See Also

- [class var cellClass: AnyClass](nsbrowser/cellclass.md)
  Returns the `NSBrowserCell` class.
- [func setCellClass(AnyClass)](nsbrowser/setcellclass(_:).md)
  Sets the class of the cell to be used by the matrices in the columns of the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/cellprototype)*