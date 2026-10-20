# numberOfItems(inSection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of items in the specified section of the snapshot.

**Availability**:
- macOS 10.15.1+

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

### Getting Item and Section Metrics
- [var numberOfItems: Int](./numberofitems.md)
  The number of items in the snapshot.
- [var numberOfSections: Int](./numberofsections.md)
  The number of sections in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/numberofitems(insection:))*