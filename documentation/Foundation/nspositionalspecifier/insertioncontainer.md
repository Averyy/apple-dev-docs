# insertionContainer

**Framework**: Foundation  
**Kind**: property

Returns the container in which the new or copied object or objects should be placed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var insertionContainer: Any? { get }
```

#### Return Value

A container. Determined by evaluating the receiver.

## See Also

- [var insertionIndex: Int](nspositionalspecifier/insertionindex.md)
  Returns an insertion index that indicates where the new or copied object or objects should be placed.
- [var insertionKey: String?](nspositionalspecifier/insertionkey.md)
  Returns the key that identifies the relationship into which the new or copied object or objects should be inserted.
- [var insertionReplaces: Bool](nspositionalspecifier/insertionreplaces.md)
  Returns a Boolean value that indicates whether evaluation has been successful and the object to be inserted should actually replace the keyed, indexed object in the insertion container.
- [var objectSpecifier: NSScriptObjectSpecifier](nspositionalspecifier/objectspecifier.md)
  Returns the object specifier specified at initialization time.
- [var position: NSPositionalSpecifier.InsertionPosition](nspositionalspecifier/position.md)
  Returns the insertion position specified at initialization time.
- [func setInsertionClassDescription(NSScriptClassDescription)](nspositionalspecifier/setinsertionclassdescription(_:).md)
  Sets the class description for the object or objects to be inserted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspositionalspecifier/insertioncontainer)*