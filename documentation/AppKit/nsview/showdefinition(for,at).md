# showDefinition(for:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Shows a window displaying the definition of the attributed string at the specified point.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func showDefinition(for attrString: NSAttributedString?, at textBaselineOrigin: NSPoint)
```

```objc
- (void) showDefinitionForAttributedString:(NSAttributedString *) attrString atPoint:(NSPoint) textBaselineOrigin;
```

#### Discussion

Shows a window that displays the definition (or other subject depending on available dictionaries) of the specified attributed string.

This method can be used for implementing the same functionality as the `NSTextView` “Look Up in Dictionary” contextual menu on a custom view.

## Parameters

- `attrString`: The attributed string for which to show the definition. If the view is an instance of NSTextView, the `attrString` can be `nil`, in which case the text view will automatically supply values suitable for displaying definitions for the specified range within its text content.
- `textBaselineOrigin`: Specifies the baseline origin of `attrString` in the view’s coordinate system.

## See Also

### Displaying Definition Windows
- [func showDefinition(for: NSAttributedString?, range: NSRange, options: [NSView.DefinitionOptionKey : Any]?, baselineOriginProvider: ((NSRange) -> NSPoint)?)](./showdefinition%28for,range,options,baselineoriginprovider%29.md)
  Shows a window displaying the definition of the specified range of the attributed string.
- [NSView.DefinitionOptionKey](./definitionoptionkey.md)
  Keys to include in your definition.
- [NSView.DefinitionPresentationType](./definitionpresentationtype.md)
  Presentation options for the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/showdefinition(for:at:))*