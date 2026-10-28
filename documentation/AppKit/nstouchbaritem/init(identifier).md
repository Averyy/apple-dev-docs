# init(identifier:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new item with the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
init(identifier: NSTouchBarItem.Identifier)
```

```objc
- (instancetype) initWithIdentifier:(NSTouchBarItemIdentifier) identifier;
```

## Discussion

The designated initializer. The identifier must be globally unique for every item, except for space items.

## See Also

### Creating a bar item
- [NSTouchBarItem.Identifier](./identifier-swift.struct.md)
  An identifier for an item in the Touch Bar.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes and returns a new item from a storyboard or nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/init(identifier:))*