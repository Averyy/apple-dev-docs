# enumerateAssets(options:using:)

**Framework**: Assets Library  
**Kind**: method

Invokes a given block using each of the assets in the group.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func enumerateAssets(options: NSEnumerationOptions = [], using enumerationBlock: ALAssetsGroupEnumerationResultsBlock!)
```

#### Discussion

## Parameters

- `options`: Options for the enumeration.
- `enumerationBlock`: The block to invoke using each of the assets in the group.

## See Also

- [func enumerateAssets(ALAssetsGroupEnumerationResultsBlock!)](alassetsgroup/enumerateassets(_:).md)
  Invokes a given block using each of the assets in the group.
- [func enumerateAssets(at: IndexSet!, options: NSEnumerationOptions, using: ALAssetsGroupEnumerationResultsBlock!)](alassetsgroup/enumerateassets(at:options:using:).md)
  Invokes a given block using each of the assets in the group at specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/enumerateassets(options:using:))*