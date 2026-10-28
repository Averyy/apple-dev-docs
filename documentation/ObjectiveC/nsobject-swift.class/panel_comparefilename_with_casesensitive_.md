# panel:compareFilename:with:caseSensitive:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Controls the ordering of files presented by the `NSSavePanel` object specified.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: There is no replacement.

## Declaration

```objc
- (NSComparisonResult) panel:(id) sender compareFilename:(NSString *) name1 with:(NSString *) name2 caseSensitive:(BOOL) caseSensitive;
```

## Return Value

One of the following:

## Discussion

- `NSOrderedAscending` if `fileName1` should precede `fileName2`
- `NSOrderedSame` if the two names are equivalent
- `NSOrderedDescending` if `fileName2` should precede `fileName1`

## Discussion

Don’t reorder filenames in the Save panel without good reason, because it may confuse the user to have files in one Save panel or Open panel ordered differently than those in other such panels or in the Finder. The default behavior of Save and Open panels is to order files as they appear in the Finder. Note also that by implementing this method you will reduce the operating performance of the panel.

## Parameters

- `sender`: Panel requesting the ordering.
- `name1`: String representing the first filename to order.
- `name2`: String representing the second filename to order.
- `caseSensitive`: If [`YES`](../yes.md), the ordering is case-sensitive; if [`NO`](../no.md), it is not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:comparefilename:with:casesensitive:)*