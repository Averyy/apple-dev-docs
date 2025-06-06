# setAssetsFilter(_:)

**Framework**: Assets Library  
**Kind**: method

Sets the filter for the group.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func setAssetsFilter(_ filter: ALAssetsFilter!)
```

#### Discussion

This method sets the filter the group; it does not execute the filter. The filter is applied when you invoke [`numberOfAssets()`](alassetsgroup/numberofassets().md) or enumerate the contents.

If you don’t set the filter, or set it to `nil`, the enumeration returns all the assets in the group.

##### Special Considerations

Only one filter is active at a time. Any enumeration currently in flight continues to completion using the previous filter.

## Parameters

- `filter`: The filter for the group.

## See Also

- [func numberOfAssets() -> Int](alassetsgroup/numberofassets.md)
  Returns the number of assets in the group that match the current filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/setassetsfilter(_:))*