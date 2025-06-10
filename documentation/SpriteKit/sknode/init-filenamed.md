# init(fileNamed:)

**Framework**: SpriteKit  
**Kind**: init

Creates a new node by loading an archive file from the game’s main bundle.

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
convenience init?(fileNamed filename: String)
```

## Mentions

- [Creating a Scene from a File](creating-a-scene-from-a-file.md)

#### Return Value

The unarchived node object.

#### Discussion

If you call this method on a subclass of the [`SKScene`](skscene.md) class and the object in the archive is an [`SKScene`](skscene.md) object, the returned object is initialized as if it is a member of the subclass. You use this behavior to create scene layouts in the Xcode Editor and provide custom behaviors in your subclass.

## Parameters

- `filename`: The name of the file, without a file extension. The file must be in the app’s main bundle and have a   filename extension.

## See Also

- [Getting Started with Nodes](getting-started-with-nodes.md)
  Learn about the fundamental properties that provide a foundation for all other nodes.
- [init()](sknode/init.md)
  Initializes a blank node.
- [init?(coder: NSCoder)](sknode/init(coder:).md)
  Called when a node is initialized from an .sks file.
- [convenience init(fileNamed: String, securelyWithClasses: Set<AnyHashable>) throws](sknode/init(filenamed:securelywithclasses:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/init(filenamed:))*