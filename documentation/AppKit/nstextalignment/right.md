# NSTextAlignment.right

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Text is right-aligned.

**Availability**:
- macOS 10.0+

## Declaration

```swift
case right
```

```c
NSTextAlignmentRight
```

## Discussion

The value of this enumeration case is `2` for binaries built for the `arm64` architecture, and running in iOS, macOS, or Simulator. The value is also `2` for binaries built for the `x86_64` architecture and running in Simulator for iOS. However, the value of this enumeration case is `1` for other binaries built for the `x86_64` architecture, including apps translated using Rosetta. If you persist this value manually, make sure to convert it for the appropriate environment when you read it.

For more information about Rosetta, see [About the Rosetta translation environment](../../apple-silicon/about-the-rosetta-translation-environment.md).

## See Also

### Constants
- [NSTextAlignment.left](./left.md)
  Text is left-aligned.
- [NSTextAlignment.center](./center.md)
  Text is center-aligned.
- [NSTextAlignment.justified](./justified.md)
  Text is justified.
- [NSTextAlignment.natural](./natural.md)
  Text uses the default alignment for the current localization of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextalignment/right)*