# numberOfItems(inSection:)

**Framework**: UIKit  
**Kind**: method

Returns the number of items in the specified section of the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func numberOfItems(inSection identifier: SectionIdentifierType) -> Int
```

#### Return Value

The number of items in the specified section. This method returns `0` if the section is empty.

#### Discussion

If you call this method with the identifier of a section that doesn’t exist in the snapshot, the app throws an error.

## Parameters

- `identifier`: The identifier of the section of the snapshot.

## See Also

- [var numberOfItems: Int](nsdiffabledatasourcesnapshot-swift.struct/numberofitems.md)
  The number of items in the snapshot.
- [var numberOfSections: Int](nsdiffabledatasourcesnapshot-swift.struct/numberofsections.md)
  The number of sections in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/numberofitems(insection:))*