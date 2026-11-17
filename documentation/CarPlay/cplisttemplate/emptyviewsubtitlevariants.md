# emptyViewSubtitleVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of localized subtitle strings to display when the list contains no items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var emptyViewSubtitleVariants: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * emptyViewSubtitleVariants;
```

## Discussion

When the list contains no items in any of its sections, the template displays an empty view with a title and a subtitle string. This property contains the potential strings to display in the subtitle position of the view. CarPlay displays the first string from the array that fits the available space, so arrange your strings in the array from most- to least-preferred.

When you update the list and add one or more items, CarPlay removes the empty view.

## See Also

### Managing an empty list
- [var showsSpinnerWhileEmpty: Bool](./showsspinnerwhileempty.md)
  A Boolean value that indicates whether to display a spinning activity indicator when the list contains no items.
- [var emptyViewTitleVariants: [String]](./emptyviewtitlevariants.md)
  An array of localized title strings to display when the list contains no items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/emptyviewsubtitlevariants)*