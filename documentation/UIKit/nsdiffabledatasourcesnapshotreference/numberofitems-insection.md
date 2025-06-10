# numberOfItems(inSection:)

**Framework**: UIKit  
**Kind**: method

Returns the number of items in the specified section of the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func numberOfItems(inSection sectionIdentifier: Any) -> Int
```

#### Return Value

The number of items in the specified section. This method returns `0` if the section is empty.

#### Discussion

If you call this method with the identifier of a section that doesn’t exist in the snapshot, the app throws an error.

## Parameters

- `sectionIdentifier`: The identifier of the section of the snapshot.

## See Also

- [var numberOfItems: Int](nsdiffabledatasourcesnapshotreference/numberofitems.md)
  The number of items in the snapshot.
- [var numberOfSections: Int](nsdiffabledatasourcesnapshotreference/numberofsections.md)
  The number of sections in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/numberofitems(insection:))*