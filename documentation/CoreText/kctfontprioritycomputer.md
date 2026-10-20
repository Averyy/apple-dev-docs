# kCTFontPriorityComputer

**Framework**: Core Text  
**Kind**: var  
**Role**: Global Variable

Priority of computer local fonts.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var kCTFontPriorityComputer: Int { get }
```

```c
kCTFontPriorityComputer
```

#### Discussion

Computer local fonts are located in `/Library/Fonts`.

## See Also

### Font Priority
- [var kCTFontPrioritySystem: Int](./kctfontprioritysystem.md)
  Priority of system fonts.
- [var kCTFontPriorityNetwork: Int](./kctfontprioritynetwork.md)
  Priority of network fonts.
- [var kCTFontPriorityUser: Int](./kctfontpriorityuser.md)
  Priority of local fonts.
- [var kCTFontPriorityDynamic: Int](./kctfontprioritydynamic.md)
  Priority of fonts registered dynamically, not located in a standard location.
- [var kCTFontPriorityProcess: Int](./kctfontpriorityprocess.md)
  Priority of fonts registered for the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontprioritycomputer)*