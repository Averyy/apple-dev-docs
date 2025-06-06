# CTFontPriority

**Framework**: Core Text  
**Kind**: typealias

The priority of font descriptors when resolving duplicates and sorting match results.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CTFontPriority = UInt32
```

#### Discussion

Use the values of this enumeration for [`kCTFontPriorityAttribute`](kctfontpriorityattribute.md).

## Topics

### Font Priority
- [var kCTFontPrioritySystem: Int](kctfontprioritysystem.md)
  Priority of system fonts.
- [var kCTFontPriorityNetwork: Int](kctfontprioritynetwork.md)
  Priority of network fonts.
- [var kCTFontPriorityComputer: Int](kctfontprioritycomputer.md)
  Priority of computer local fonts.
- [var kCTFontPriorityUser: Int](kctfontpriorityuser.md)
  Priority of local fonts.
- [var kCTFontPriorityDynamic: Int](kctfontprioritydynamic.md)
  Priority of fonts registered dynamically, not located in a standard location.
- [var kCTFontPriorityProcess: Int](kctfontpriorityprocess.md)
  Priority of fonts registered for the process.

## See Also

- [let kCTFontPriorityAttribute: CFString](kctfontpriorityattribute.md)
  The font priority used by font descriptors when resolving duplicates and sorting match results.
- [Font Attributes](font-attributes.md)
  The keys for accessing font attributes from a font descriptor.
- [enum CTFontOrientation](ctfontorientation.md)
  The intended rendering orientation of the font for obtaining glyph metrics.
- [enum CTFontFormat](ctfontformat.md)
  The recognized format of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontpriority)*