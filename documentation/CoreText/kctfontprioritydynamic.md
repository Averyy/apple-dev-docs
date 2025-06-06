# kCTFontPriorityDynamic

**Framework**: Core Text  
**Kind**: var

Priority of fonts registered dynamically, not located in a standard location.

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
var kCTFontPriorityDynamic: Int { get }
```

#### Discussion

Dynamic fonts are either in [`user`](ctfontmanagerscope/user.md) or [`CTFontManagerScope.session`](ctfontmanagerscope/session.md).

## See Also

- [var kCTFontPrioritySystem: Int](kctfontprioritysystem.md)
  Priority of system fonts.
- [var kCTFontPriorityNetwork: Int](kctfontprioritynetwork.md)
  Priority of network fonts.
- [var kCTFontPriorityComputer: Int](kctfontprioritycomputer.md)
  Priority of computer local fonts.
- [var kCTFontPriorityUser: Int](kctfontpriorityuser.md)
  Priority of local fonts.
- [var kCTFontPriorityProcess: Int](kctfontpriorityprocess.md)
  Priority of fonts registered for the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontprioritydynamic)*