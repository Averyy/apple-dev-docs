# NSTextLayoutFragment.EnumerationOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSTextLayoutFragmentEnumerationOptions : NSUInteger;
```

## Topics

### Creating a layout fragment enumeration
- [init(rawValue: UInt)](./enumerationoptions/init%28rawvalue%29.md)
  Creates an instance of the enumeration with the provided unsigned integer value.
### Layout fragment characteristics
- [static var ensuresExtraLineFragment: NSTextLayoutFragment.EnumerationOptions](./enumerationoptions/ensuresextralinefragment.md)
  Synthesize the extra line fragment when necessary.
- [static var ensuresLayout: NSTextLayoutFragment.EnumerationOptions](./enumerationoptions/ensureslayout.md)
  When enumerating, tell the layout fragments to layout their contents.
- [static var estimatesSize: NSTextLayoutFragment.EnumerationOptions](./enumerationoptions/estimatessize.md)
  When enumerating, tell the layout fragments to estimate their size.
- [static var reverse: NSTextLayoutFragment.EnumerationOptions](./enumerationoptions/reverse.md)
  Causes the enumeration to start from the last element.
- [NSTextLayoutFragmentEnumerationOptionsNone](../nstextlayoutfragmentenumerationoptions/nstextlayoutfragmentenumerationoptionsnone.md)
  The value that represents no selected enumeration options.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Accessing and updating the text
- [func enumerateTextElements(from: (any NSTextLocation)?, options: NSTextContentManager.EnumerationOptions, using: (NSTextElement) -> Bool) -> (any NSTextLocation)?](../nstextelementprovider/enumeratetextelements%28from,options,using%29.md)
  Enumerates text elements starting at the text location you provide.
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](../nstextelementprovider/location%28_,offsetby%29.md)
  Returns a new location from location with offset you provide.
- [func replaceContents(in: NSTextRange, with: [NSTextElement]?)](../nstextelementprovider/replacecontents%28in,with%29.md)
  Replaces the characters specified by range with the text elements you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/enumerationoptions)*