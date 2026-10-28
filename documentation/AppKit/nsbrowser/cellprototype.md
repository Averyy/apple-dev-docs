# cellPrototype

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The prototype `NSCell` for displaying items in the matrices in the columns of the browser.

**Availability**:
- macOS

## Declaration

```swift
var cellPrototype: Any! { get set }
```

```objc
@property (strong, null_resettable) id cellPrototype;
```

## Discussion

The prototype `NSCell` instance is copied to display items in the matrices of the browser.

## See Also

### Managing Component Types
- [class var cellClass: AnyClass](./cellclass.md)
  Returns the `NSBrowserCell` class.
- [func setCellClass(AnyClass)](./setcellclass%28_%29.md)
  Sets the class of the cell to be used by the matrices in the columns of the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/cellprototype)*