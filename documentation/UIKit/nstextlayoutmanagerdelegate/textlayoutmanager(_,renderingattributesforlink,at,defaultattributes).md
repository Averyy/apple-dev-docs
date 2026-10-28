# textLayoutManager(_:renderingAttributesForLink:at:defaultAttributes:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

The method the framework calls to return a dictionary of attributes for rendering a link attribute name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, renderingAttributesForLink link: Any, at location: any NSTextLocation, defaultAttributes renderingAttributes: [NSAttributedString.Key : Any] = [:]) -> [NSAttributedString.Key : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) textLayoutManager:(NSTextLayoutManager *) textLayoutManager renderingAttributesForLink:(id) link atLocation:(id<NSTextLocation>) location defaultAttributes:(NSDictionary<NSString *,id> *) renderingAttributes;
```

## Return Value

A dictionary of  attributes.

## Parameters

- `textLayoutManager`: The `NSTextLayoutManager`.
- `link`: The link.
- `location`: The [`NSTextLocation`](../nstextlocation.md) of the link.
- `renderingAttributes`: A dictionary of attributes whose keys are [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md) values.

## See Also

### Responding to layout changes
- [func textLayoutManager(NSTextLayoutManager, shouldBreakLineBefore: any NSTextLocation, hyphenating: Bool) -> Bool](./textlayoutmanager%28_,shouldbreaklinebefore,hyphenating%29.md)
  The method the framework calls to determine the soft line break point.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](./textlayoutmanager%28_,textlayoutfragmentfor,in%29.md)
  The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:))*