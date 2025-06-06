# accessibilityRowRange()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the visible range of rows.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityRowRange() -> NSRange
```

#### Return Value

The visible range of rows.

#### Discussion

Set the location of the range to the first row containing the cell. Use the length of the range to specify the number of rows that the cell spans. If you do not implement this method, the system assumes an initial index of [`NSNotFound`](https://developer.apple.com/documentation/foundation/nsnotfound-8f9) and a length of `0`.

## See Also

- [func accessibilityColumnRange() -> NSRange](uiaccessibilitycontainerdatatablecell/accessibilitycolumnrange.md)
  Returns the columns spanned by the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatablecell/accessibilityrowrange())*