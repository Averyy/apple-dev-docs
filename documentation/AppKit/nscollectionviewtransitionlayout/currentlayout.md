# currentLayout

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The collection view’s current layout object.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var currentLayout: NSCollectionViewLayout { get }
```

```objc
@property (readonly) NSCollectionViewLayout * currentLayout;
```

#### Discussion

Use this object to retrieve the initial layout attributes for elements of the collection view. If the transition is ultimately cancelled, the collection view animates its items back to the attributes provided by this object.

## See Also

### Accessing the Layout Objects
- [var nextLayout: NSCollectionViewLayout](./nextlayout.md)
  The collection view’s new layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/currentlayout)*