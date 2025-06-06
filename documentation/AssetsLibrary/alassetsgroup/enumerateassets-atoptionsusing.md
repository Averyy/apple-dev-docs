# enumerateAssets(at:options:using:)

**Framework**: Assets Library  
**Kind**: method

Invokes a given block using each of the assets in the group at specified indexes.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func enumerateAssets(at indexSet: IndexSet!, options: NSEnumerationOptions = [], using enumerationBlock: ALAssetsGroupEnumerationResultsBlock!)
```

#### Discussion

## Parameters

- `indexSet`: The index set must not specify any indexes exceeding  .
- `options`: Options for the enumeration.
- `enumerationBlock`: The block to invoke using each of the assets in the group at the indexes in  .

## See Also

- [func enumerateAssets(ALAssetsGroupEnumerationResultsBlock!)](alassetsgroup/enumerateassets(_:).md)
  Invokes a given block using each of the assets in the group.
- [func enumerateAssets(options: NSEnumerationOptions, using: ALAssetsGroupEnumerationResultsBlock!)](alassetsgroup/enumerateassets(options:using:).md)
  Invokes a given block using each of the assets in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/enumerateassets(at:options:using:))*