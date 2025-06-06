# insertionKey

**Framework**: Foundation  
**Kind**: property

Returns the key that identifies the relationship into which the new or copied object or objects should be inserted.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var insertionKey: String? { get }
```

#### Return Value

A key. Determined by evaluating the receiver.

## See Also

- [var insertionContainer: Any?](nspositionalspecifier/insertioncontainer.md)
  Returns the container in which the new or copied object or objects should be placed.
- [var insertionIndex: Int](nspositionalspecifier/insertionindex.md)
  Returns an insertion index that indicates where the new or copied object or objects should be placed.
- [var insertionReplaces: Bool](nspositionalspecifier/insertionreplaces.md)
  Returns a Boolean value that indicates whether evaluation has been successful and the object to be inserted should actually replace the keyed, indexed object in the insertion container.
- [var objectSpecifier: NSScriptObjectSpecifier](nspositionalspecifier/objectspecifier.md)
  Returns the object specifier specified at initialization time.
- [var position: NSPositionalSpecifier.InsertionPosition](nspositionalspecifier/position.md)
  Returns the insertion position specified at initialization time.
- [func setInsertionClassDescription(NSScriptClassDescription)](nspositionalspecifier/setinsertionclassdescription(_:).md)
  Sets the class description for the object or objects to be inserted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspositionalspecifier/insertionkey)*