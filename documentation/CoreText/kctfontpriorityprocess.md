# kCTFontPriorityProcess

**Framework**: Core Text  
**Kind**: var

Priority of fonts registered for the process.

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
var kCTFontPriorityProcess: Int { get }
```

#### Discussion

Fonts registered for the process are in [`CTFontManagerScope.process`](ctfontmanagerscope/process.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontpriorityprocess)*