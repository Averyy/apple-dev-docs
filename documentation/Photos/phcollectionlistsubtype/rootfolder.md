# PHCollectionListSubtype.rootFolder

**Framework**: Photos  
**Kind**: case  
**Role**: Case

The collection list that contains the top-level user collections.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case rootFolder
```

```c
PHCollectionListSubtypeRootFolder
```

## Discussion

There is always one root folder in the library and does not allow [`PHCollectionEditOperation.rename`](../phcollectioneditoperation/rename.md) or [`PHCollectionEditOperation.delete`](../phcollectioneditoperation/delete.md)

## See Also

### Constants
- [PHCollectionListSubtype.momentListCluster](./momentlistcluster.md)
  The collection list is a moment cluster, grouping several related moments.
- [PHCollectionListSubtype.momentListYear](./momentlistyear.md)
  The collection list is a moment year, grouping all moments from one or more calendar years.
- [PHCollectionListSubtype.regularFolder](./regularfolder.md)
  The collection list is a folder containing albums or other folders.
- [PHCollectionListSubtype.smartFolderEvents](./smartfolderevents.md)
  The collection list is a smart folder containing one or more Events synced from a Mac.
- [PHCollectionListSubtype.smartFolderFaces](./smartfolderfaces.md)
  The collection list is a smart folder containing one or more Faces groups synced from a Mac.
- [PHCollectionListSubtype.any](./any.md)
  Use this value to fetch collection lists of all possible subtypes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistsubtype/rootfolder)*