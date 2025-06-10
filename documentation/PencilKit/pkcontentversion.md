# PKContentVersion

**Framework**: PencilKit  
**Kind**: enum

Constants that represent versions of PencilKit for backward compatibility.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum PKContentVersion
```

## Mentions

- [Supporting backward compatibility for ink types](supporting-backward-compatibility-for-ink-types.md)

## Topics

### Latest version
- [static var latest: PKContentVersion](pkcontentversion/latest.md)
  A property that returns latest version of PencilKit, which supports all currently available inks.
### Specific versions
- [PKContentVersion.version1](pkcontentversion/version1.md)
  The PencilKit version that supports inks from iPadOS 14 and earlier, including marker, pen, and pencil.
- [PKContentVersion.version2](pkcontentversion/version2.md)
  The PencilKit version that supports inks from iPadOS 17 and earlier, including marker, pen, pencil, monoline, fountain pen, watercolor, and crayon.
- [PKContentVersion.version3](pkcontentversion/version3.md)
  The PencilKit version that supports barrel-roll angle data in inks.
### Enumeration Cases
- [PKContentVersion.version4](pkcontentversion/version4.md)
  New Reed Pen
### Initializers
- [init?(rawValue: Int)](pkcontentversion/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Supporting backward compatibility for ink types](supporting-backward-compatibility-for-ink-types.md)
  Leverage the latest PencilKit features while providing a good user experience in earlier versions of the OS that don’t support those features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcontentversion)*