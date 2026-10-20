# accessibilityColumnRange()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the columns spanned by the cell.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func accessibilityColumnRange() -> NSRange
```

```objc
- (NSRange) accessibilityColumnRange;
```

#### Return Value

The column or columns that the cell spans.

#### Discussion

Set the location of the range to the first column containing the cell. Use the length of the range to specify the number of columns that the cell spans. If you do not implement this method, the system assumes an initial index of [`NSNotFound`](../../Foundation/nsnotfound-9t5v2.md) and a length of `0`.

## See Also

### Getting the rows and columns
- [func accessibilityRowRange() -> NSRange](./accessibilityrowrange%28%29.md)
  Returns the visible range of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatablecell/accessibilitycolumnrange())*