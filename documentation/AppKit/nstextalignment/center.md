# NSTextAlignment.center

**Framework**: AppKit  
**Kind**: case

Text is center-aligned.

**Availability**:
- macOS 10.0+

## Declaration

```swift
case center
```

#### Discussion

The value of this enumeration case is `1` for binaries built for the `arm64` architecture, and running in iOS, macOS, or Simulator. The value is also `1` for binaries built for the `x86_64` architecture and running in Simulator for iOS. However, the value of this enumeration case is `2` for other binaries built for the `x86_64` architecture, including apps translated using Rosetta. If you persist this value manually, make sure to convert it for the appropriate environment when you read it.

For more information about Rosetta, see [`About the Rosetta translation environment`](https://developer.apple.com/documentation/Apple-Silicon/about-the-rosetta-translation-environment).

## See Also

- [NSTextAlignment.left](nstextalignment/left.md)
  Text is left-aligned.
- [NSTextAlignment.right](nstextalignment/right.md)
  Text is right-aligned.
- [NSTextAlignment.justified](nstextalignment/justified.md)
  Text is justified.
- [NSTextAlignment.natural](nstextalignment/natural.md)
  Text uses the default alignment for the current localization of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextalignment/center)*