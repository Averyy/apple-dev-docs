# layoutCharacters(in:for:maximumNumberOfLineFragments:)

**Framework**: AppKit  
**Kind**: method

Lays out characters in the given character range for the specified layout manager.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func layoutCharacters(in characterRange: NSRange, for layoutManager: NSLayoutManager, maximumNumberOfLineFragments maxNumLines: Int) -> NSRange
```

#### Return Value

The method returns the actual character range that the receiving `NSTypesetter` processed.

#### Discussion

The layout process can be interrupted when the number of line fragments exceeds `maxNumLines`.

## Parameters

- `characterRange`: The range of the characters to lay out.
- `layoutManager`: The layout manager that does the drawing.
- `maxNumLines`: The maximum number of line fragments to lay out. Specify   for unlimited number of line fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/layoutcharacters(in:for:maximumnumberoflinefragments:))*