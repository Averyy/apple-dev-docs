# enumerateObjects(options:using:)

**Framework**: Foundation  
**Kind**: method

Executes a given closure or block using each object in the array with the specified options.

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
func enumerateObjects(options opts: NSEnumerationOptions = [], using block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

This method executes synchronously. By default, the enumeration starts with the first object and continues serially through the array to the last object. You can specify [`concurrent`](nsenumerationoptions/concurrent.md) and/or [`reverse`](nsenumerationoptions/reverse.md) as enumeration options to modify this behavior.

## Parameters

- `opts`: The options for the enumeration. For possible values, see  .
- `block`: A closure or block to execute for each object in the array, taking three arguments:

## See Also

- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsarray/enumerateobjects(_:).md)
  Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsarray/enumerateobjects(at:options:using:).md)
  Executes a given block using the objects in the array at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/enumerateobjects(options:using:))*