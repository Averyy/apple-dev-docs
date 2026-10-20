# isVisible(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the specified item is currently visible onscreen.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func isVisible(_ item: Any) -> Bool
```

```objc
- (BOOL) isVisible:(ItemIdentifierType) item;
```

## See Also

### Getting item metrics
- [func index(ofItem: Any) -> Int](./index%28ofitem%29.md)
  Finds the index of the specified item in the section snapshot.
- [func level(ofItem: Any) -> Int](./level%28ofitem%29.md)
  Finds the hierarchical level of the specified item in the section snapshot.
- [func parent(ofChildItem: Any) -> Any?](./parent%28ofchilditem%29.md)
  Finds the parent item of the specified item in the section snapshot.
- [func containsItem(Any) -> Bool](./containsitem%28_%29.md)
  Indicates whether the section snapshot contains the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/isvisible(_:))*