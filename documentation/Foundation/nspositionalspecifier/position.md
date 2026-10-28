# position

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the insertion position specified at initialization time.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var position: NSPositionalSpecifier.InsertionPosition { get }
```

```objc
@property (readonly) NSInsertionPosition position;
```

## Return Value

An insertion position.

## See Also

### Accessing information about a positional specifier
- [var insertionContainer: Any?](./insertioncontainer.md)
  Returns the container in which the new or copied object or objects should be placed.
- [var insertionIndex: Int](./insertionindex.md)
  Returns an insertion index that indicates where the new or copied object or objects should be placed.
- [var insertionKey: String?](./insertionkey.md)
  Returns the key that identifies the relationship into which the new or copied object or objects should be inserted.
- [var insertionReplaces: Bool](./insertionreplaces.md)
  Returns a Boolean value that indicates whether evaluation has been successful and the object to be inserted should actually replace the keyed, indexed object in the insertion container.
- [var objectSpecifier: NSScriptObjectSpecifier](./objectspecifier.md)
  Returns the object specifier specified at initialization time.
- [func setInsertionClassDescription(NSScriptClassDescription)](./setinsertionclassdescription%28_%29.md)
  Sets the class description for the object or objects to be inserted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspositionalspecifier/position)*