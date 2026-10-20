# numberOfItems(inSection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of items in the specified section.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func numberOfItems(inSection section: Int) -> Int
```

```objc
- (NSInteger) numberOfItemsInSection:(NSInteger) section;
```

#### Return Value

The number of items in the section.

#### Discussion

Use this method to get the number of items currently displayed by the collection view for the specified section. Do not call the methods of the data source to get this information.

## Parameters

- `section`: The index of the section whose item count you want. This index is 0-based.

## See Also

### Getting the State of the Collection View
- [var numberOfSections: Int](./numberofsections.md)
  The number of sections in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/numberofitems(insection:))*