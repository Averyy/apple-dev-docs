# showsSpinnerWhileEmpty

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to display a spinning activity indicator when the list contains no items.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var showsSpinnerWhileEmpty: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL showsSpinnerWhileEmpty;
```

## Discussion

If the value of this property is `true` and the list contains no items, the list interface displays a spinning activity indicator in addition to content from the [`emptyViewTitleVariants`](./emptyviewtitlevariants.md) and [`emptyViewSubtitleVariants`](./emptyviewsubtitlevariants.md) properties. You might enable this property if you display your list interface first and load its contents asynchronously.

## See Also

### Managing an empty list
- [var emptyViewTitleVariants: [String]](./emptyviewtitlevariants.md)
  An array of localized title strings to display when the list contains no items.
- [var emptyViewSubtitleVariants: [String]](./emptyviewsubtitlevariants.md)
  An array of localized subtitle strings to display when the list contains no items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/showsspinnerwhileempty)*