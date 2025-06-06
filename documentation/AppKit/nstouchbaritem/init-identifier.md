# init(identifier:)

**Framework**: AppKit  
**Kind**: init

Creates a new item with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
init(identifier: NSTouchBarItem.Identifier)
```

#### Discussion

The designated initializer. The identifier must be globally unique for every item, except for space items.

## See Also

- [NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct.md)
  An identifier for an item in the Touch Bar.
- [init?(coder: NSCoder)](nstouchbaritem/init(coder:).md)
  Initializes and returns a new item from a storyboard or nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/init(identifier:))*