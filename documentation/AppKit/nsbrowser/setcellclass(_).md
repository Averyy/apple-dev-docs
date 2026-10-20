# setCellClass(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the class of the cell to be used by the matrices in the columns of the browser.

**Availability**:
- macOS

## Declaration

```swift
func setCellClass(_ factoryId: AnyClass)
```

```objc
- (void) setCellClass:(Class) factoryId;
```

## Parameters

- `factoryId`: The class of `NSCell` used by the matrices in the columns of the browser. This method creates an instance of the class and sets [`cellPrototype`](./cellprototype.md).

## See Also

### Managing Component Types
- [class var cellClass: AnyClass](./cellclass.md)
  Returns the `NSBrowserCell` class.
- [var cellPrototype: Any!](./cellprototype.md)
  The prototype `NSCell` for displaying items in the matrices in the columns of the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setcellclass(_:))*