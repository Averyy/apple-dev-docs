# index(ofItem:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Finds the index of the specified item in the section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func index(ofItem item: Any) -> Int
```

```objc
- (NSInteger) indexOfItem:(ItemIdentifierType) item;
```

## See Also

### Getting item metrics
- [func level(ofItem: Any) -> Int](./level%28ofitem%29.md)
  Finds the hierarchical level of the specified item in the section snapshot.
- [func parent(ofChildItem: Any) -> Any?](./parent%28ofchilditem%29.md)
  Finds the parent item of the specified item in the section snapshot.
- [func containsItem(Any) -> Bool](./containsitem%28_%29.md)
  Indicates whether the section snapshot contains the specified item.
- [func isVisible(Any) -> Bool](./isvisible%28_%29.md)
  Indicates whether the specified item is currently visible onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/index(ofitem:))*