# enumerateObjects(_:)

**Framework**: Foundation  
**Kind**: method

Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateObjects(_ block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

This method executes synchronously. Values allocated within the block are deallocated after the block is executed.

## Parameters

- `block`: A closure or block to execute for each object in the array, taking three arguments:

## See Also

- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsarray/enumerateobjects(options:using:).md)
  Executes a given closure or block using each object in the array with the specified options.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsarray/enumerateobjects(at:options:using:).md)
  Executes a given block using the objects in the array at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/enumerateobjects(_:))*