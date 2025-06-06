# enumerateTextElements(from:options:using:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Enumerates text elements starting at the text location you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func enumerateTextElements(from textLocation: (any NSTextLocation)?, options: NSTextContentManager.EnumerationOptions = [], using block: (NSTextElement) -> Bool) -> (any NSTextLocation)?
```

#### Return Value

An `NSTextLocation`.

#### Discussion

If `textLocation` is `nil`, the method uses `documentRange.location` for forward enumeration and `documentRange.endLocation` for reverse enumeration. When enumerating backward, the method starts with the element preceding the one containing `textLocation`. If enumerated at least one element, it returns the edge of the enumerated range.

The enumerated range might not match the range of the last element returned. It enumerates the elements in the sequence, but it can skip a range (it can limit the maximum number of text elements enumerated for a single invocation or hide some elements from the layout).

Returning `NO` or `false` from block breaks out of the enumeration.

## Parameters

- `textLocation`: The   at which to start the enumeration.
- `options`: One of the possible   directions.
- `block`: A block you use to evaluate whether to continue the enumeration or tell the method to stop. Return   to end the enumeration process.

## See Also

- [NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextelementprovider/location(_:offsetby:).md)
  Returns a new location from location with offset you provide.
- [func replaceContents(in: NSTextRange, with: [NSTextElement]?)](nstextelementprovider/replacecontents(in:with:).md)
  Replaces the characters specified by range with the text elements you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelementprovider/enumeratetextelements(from:options:using:))*