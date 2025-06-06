# NSTextLayoutFragment.EnumerationOptions

**Framework**: UIKit  
**Kind**: struct

Values that describe options for enumerating text layout fragments.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct EnumerationOptions
```

## Topics

### Creating a layout fragment enumeration
- [init(rawValue: UInt)](nstextlayoutfragment/enumerationoptions/init(rawvalue:).md)
  Creates an instance of the enumeration with the provided unsigned integer value.
### Layout fragment characteristics
- [static var ensuresExtraLineFragment: NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions/ensuresextralinefragment.md)
  Synthesize the extra line fragment when necessary.
- [static var ensuresLayout: NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions/ensureslayout.md)
  When enumerating, tell the layout fragments to layout their contents.
- [static var estimatesSize: NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions/estimatessize.md)
  When enumerating, tell the layout fragments to estimate their size.
- [static var reverse: NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions/reverse.md)
  Causes the enumeration to start from the last element.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func enumerateTextElements(from: (any NSTextLocation)?, options: NSTextContentManager.EnumerationOptions, using: (NSTextElement) -> Bool) -> (any NSTextLocation)?](nstextelementprovider/enumeratetextelements(from:options:using:).md)
  Enumerates text elements starting at the text location you provide.
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextelementprovider/location(_:offsetby:).md)
  Returns a new location from location with offset you provide.
- [func replaceContents(in: NSTextRange, with: [NSTextElement]?)](nstextelementprovider/replacecontents(in:with:).md)
  Replaces the characters specified by range with the text elements you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/enumerationoptions)*