# isLexicallyNormal

**Framework**: System  
**Kind**: property

Whether the path is in lexical-normal form, that is `.` and `..` components have been collapsed lexically (i.e. without following symlinks).

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var isLexicallyNormal: Bool { get }
```

#### Discussion

Examples:

- `"/usr/local/bin".isLexicallyNormal == true`
- `"../local/bin".isLexicallyNormal   == true`
- `"local/bin/..".isLexicallyNormal   == false`


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/islexicallynormal)*