# nextLayout

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The collection view’s new layout object.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var nextLayout: NSCollectionViewLayout { get }
```

```objc
@property (readonly) NSCollectionViewLayout * nextLayout;
```

#### Discussion

Use this object to retrieve the final layout attributes for elements of the collection view. If the transition completes as expected, the collection view animates its items to the attributes provided by this object.

## See Also

### Accessing the Layout Objects
- [var currentLayout: NSCollectionViewLayout](./currentlayout.md)
  The collection view’s current layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/nextlayout)*