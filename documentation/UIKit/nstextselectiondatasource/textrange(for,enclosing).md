# textRange(for:enclosing:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a text range that corresponds to selection granularity of the enclosing location.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func textRange(for selectionGranularity: NSTextSelection.Granularity, enclosing location: any NSTextLocation) -> NSTextRange?
```

```objc
- (NSTextRange *) textRangeForSelectionGranularity:(NSTextSelectionGranularity) selectionGranularity enclosingLocation:(id<NSTextLocation>) location;
```

#### Return Value

Returns the text range of the section, or `nil` when `documentRange.isEmpty` `true`.

## Parameters

- `selectionGranularity`: One of the possible [`NSTextSelection.Granularity`](../nstextselection/granularity-swift.enum.md) options.
- `location`: A location that encloses the text range of interest.

## See Also

### Finding specific content in the selection
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](./location%28_,offsetby%29.md)
  Returns a new location using the location and offset you specify.
- [func lineFragmentRange(for: CGPoint, inContainerAt: any NSTextLocation) -> NSTextRange?](./linefragmentrange%28for,incontainerat%29.md)
  Returns the range of the line fragment that contains the point you specify.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](./offset%28from,to%29.md)
  Returns the offset between the two locations you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/textrange(for:enclosing:))*