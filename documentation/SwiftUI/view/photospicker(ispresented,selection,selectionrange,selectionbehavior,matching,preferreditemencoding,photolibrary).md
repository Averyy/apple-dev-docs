# photosPicker(isPresented:selection:selectionRange:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library, constrained to a range of selection counts.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func photosPicker<R>(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, selectionRange: R, selectionBehavior: PhotosPickerSelectionBehavior = .default, matching filter: PHPickerFilter? = nil, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic, photoLibrary: PHPhotoLibrary) -> some View where R : RangeExpression, R.Bound == Int
```

## Discussion

The user explicitly grants access only to items they choose, so photo library access authorization is not needed.

## Parameters

- `isPresented`: The binding to whether the Photos picker should be shown.
- `selection`: All items being shown and selected in the Photos picker.
- `selectionRange`: The number of items that can be selected. For example, `1...10` requires between 1 and 10 items, `3...` requires at least 3 items without an upper limit, and `...5` allows up to 5 items with the default minimum. An upper bound below 1 is treated as 1, and a lower bound above the upper bound is lowered to it.
- `selectionBehavior`: The selection behavior of the Photos picker. Default is `.default`.
- `filter`: Types of items that can be shown. Default is `nil`. Setting it to `nil` means all supported types can be shown.
- `preferredItemEncoding`: The encoding disambiguation policy of selected items. Default is `.automatic`. Setting it to `.automatic` means the best encoding determined by the system will be used.
- `photoLibrary`: The photo library to choose from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photospicker(ispresented:selection:selectionrange:selectionbehavior:matching:preferreditemencoding:photolibrary:))*