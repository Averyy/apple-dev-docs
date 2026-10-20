# symbolicTraits

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A bit mask that describes the traits of the receiver.

**Availability**:
- macOS

## Declaration

```swift
var symbolicTraits: NSFontDescriptor.SymbolicTraits { get }
```

```objc
@property (readonly) NSFontDescriptorSymbolicTraits symbolicTraits;
```

## See Also

### Related Documentation
- [var fontAttributes: [NSFontDescriptor.AttributeName : Any]](./fontattributes.md)
  The receiver’s dictionary of attributes.
- [var postscriptName: String?](./postscriptname.md)
  The PostScript name of the receiver.
### Getting the Font Traits
- [typealias NSFontSymbolicTraits](../nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.
- [NSFontDescriptor.TraitKey](./traitkey.md)
  Constants that can be used as keys to retrieve information about a font descriptor from its trait dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/symbolictraits-swift.property)*