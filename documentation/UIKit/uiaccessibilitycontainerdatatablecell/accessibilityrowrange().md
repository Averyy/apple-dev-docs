# accessibilityRowRange()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
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
func accessibilityRowRange() -> NSRange
```

```objc
- (NSRange) accessibilityRowRange;
```

#### Return Value

The visible range of rows.

#### Discussion

Set the location of the range to the first row containing the cell. Use the length of the range to specify the number of rows that the cell spans. If you do not implement this method, the system assumes an initial index of [`NSNotFound`](../../Foundation/nsnotfound-9t5v2.md) and a length of `0`.

## See Also

### Getting the rows and columns
- [func accessibilityColumnRange() -> NSRange](./accessibilitycolumnrange%28%29.md)
  Returns the columns spanned by the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatablecell/accessibilityrowrange())*