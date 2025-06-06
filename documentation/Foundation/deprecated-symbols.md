# Deprecated Symbols

**Framework**: Foundation

Migrate your code away from using these symbols.

## Topics

### Deprecated Initializers
- [init?(path: String, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(path:documentattributes:).md)
  Initializes a new attribute string object from RTF or RTFD data in the file at the specified path.
- [init?(URL: URL, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(url:documentattributes:).md)
  Initializes a new attributed string object from the data at the specified URL.
- [init(fileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsattributedstring/init(fileurl:options:documentattributes:).md)
  Initializes a new attributed string object from the data at the specified URL.
### Deprecated Properties
- [var containsAttachments: Bool](nsattributedstring/containsattachments.md)
  A Boolean value that indicates whether the attribute string contains any attachment attributes.
### Deprecated Enumerations
- [enum NSTextWritingDirection](../UIKit/NSTextWritingDirection.md)
  Options for specifying text-writing direction.
### Deprecated Instance Methods
- [func url(at: Int, effectiveRange: NSRangePointer) -> URL?](nsattributedstring/url(at:effectiverange:).md)
  Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection.
- [func draw(with: NSRect, options: NSString.DrawingOptions)](nsattributedstring/draw(with:options:).md)
  Draws the attributed string with the specified options within the specified rectangle in the current graphics context.
- [func boundingRect(with: NSSize, options: NSString.DrawingOptions) -> NSRect](nsattributedstring/boundingrect(with:options:).md)
  Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/deprecated-symbols)*