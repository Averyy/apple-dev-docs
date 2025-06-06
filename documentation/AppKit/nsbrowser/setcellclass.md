# setCellClass(_:)

**Framework**: AppKit  
**Kind**: method

Sets the class of the cell to be used by the matrices in the columns of the browser.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setCellClass(_ factoryId: AnyClass)
```

## Parameters

- `factoryId`: The class of   used by the matrices in the columns of the browser. This method creates an instance of the class and sets  .

## See Also

- [class var cellClass: AnyClass](nsbrowser/cellclass.md)
  Returns the `NSBrowserCell` class.
- [var cellPrototype: Any!](nsbrowser/cellprototype.md)
  The prototype `NSCell` for displaying items in the matrices in the columns of the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setcellclass(_:))*