# Deprecated Symbols

**Framework**: Foundation  
**Role**: API Collection

Migrate your code away from using these symbols.

## Topics

### Deprecated Initializers
- [init?(path: String, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsattributedstring/init%28path,documentattributes%29.md)
  Initializes a new attribute string object from RTF or RTFD data in the file at the specified path.
- [init?(URL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsattributedstring/init%28url,documentattributes%29.md)
  Initializes a new attributed string object from the data at the specified URL.
- [init(fileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](./nsattributedstring/init%28fileurl,options,documentattributes%29.md)
  Initializes a new attributed string object from the data at the specified URL.
### Deprecated Properties
- [var containsAttachments: Bool](./nsattributedstring/containsattachments.md)
  A Boolean value that indicates whether the attribute string contains any attachment attributes.
- [+ textFileTypes](./nsattributedstring/textfiletypes.md)
  Returns an array of strings that represent file types that can be loaded as text.
- [+ textUnfilteredFileTypes](./nsattributedstring/textunfilteredfiletypes.md)
  Returns an array of strings that represent file types that can be loaded as a text.
- [+ textPasteboardTypes](./nsattributedstring/textpasteboardtypes.md)
  Returns an array of pasteboard types that can be loaded as text.
- [+ textUnfilteredPasteboardTypes](./nsattributedstring/textunfilteredpasteboardtypes.md)
  Returns an array of pasteboard types that can be loaded as text.
### Deprecated Enumerations
- [enum NSTextWritingDirection](../UIKit/nstextwritingdirection.md)
  Options for specifying text-writing direction.
### Deprecated Instance Methods
- [func url(at: Int, effectiveRange: NSRangePointer) -> URL?](./nsattributedstring/url%28at,effectiverange%29.md)
  Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection.
- [func draw(with: NSRect, options: NSString.DrawingOptions)](./nsattributedstring/draw%28with,options%29.md)
  Draws the attributed string with the specified options within the specified rectangle in the current graphics context.
- [func boundingRect(with: NSSize, options: NSString.DrawingOptions) -> NSRect](./nsattributedstring/boundingrect%28with,options%29.md)
  Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context.
### Deprecated Constants
- [NSUnderlineByWordMask](../AppKit/nsunderlinebywordmask.md)
  Draw the underline only underneath words, not underneath whitespace.
- [NSUnderlineStrikethroughMask](../AppKit/nsunderlinestrikethroughmask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/deprecated-symbols)*