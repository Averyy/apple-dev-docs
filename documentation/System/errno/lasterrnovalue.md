# lastErrnoValue

**Framework**: System  
**Kind**: property  
**Role**: Type Property

The largest valid error.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var lastErrnoValue: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

This value is the largest valid value encountered using the C `errno` global variable. It isn’t a valid error.

The corresponding C error is `ELAST`.

## See Also

### Reserved
- [static var multiHop: Errno](./multihop.md)
  Reserved.
- [static var noLink: Errno](./nolink.md)
  Reserved.
- [static var noStreamResources: Errno](./nostreamresources.md)
  Reserved.
- [static var notStream: Errno](./notstream.md)
  Reserved.
- [static var notUsed: Errno](./notused.md)
  Error. Not used.
- [static var timeout: Errno](./timeout.md)
  Reserved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/lasterrnovalue)*