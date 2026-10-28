# UIContentInsetsReference.automatic

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

Content insets use the system default reference point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case automatic
```

```c
UIContentInsetsReferenceAutomatic
```

## Discussion

When you set this value on a section in a collection view, the section defaults to using the content insets reference value of the collection view.

## See Also

### Constants
- [UIContentInsetsReference.none](./none.md)
  Content insets don’t have a reference point in relation to other insets.
- [UIContentInsetsReference.safeArea](./safearea.md)
  Content insets use a reference point in relation to the safe area.
- [UIContentInsetsReference.layoutMargins](./layoutmargins.md)
  Content insets use a reference point in relation to the layout margins.
- [UIContentInsetsReference.readableContent](./readablecontent.md)
  Content insets use a reference point in relation to the readable content guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentinsetsreference/automatic)*