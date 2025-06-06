# enumerateObjects(at:options:using:)

**Framework**: Foundation  
**Kind**: method

Executes a given block using the objects in the array at the specified indexes.

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
func enumerateObjects(at s: IndexSet, options opts: NSEnumerationOptions = [], using block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

By default, the enumeration starts with the first object and continues serially through the array to the last element specified by `indexSet`. You can specify `NSEnumerationConcurrent` and/or `NSEnumerationReverse` as enumeration options to modify this behavior.

This method executes synchronously.

> ❗ **Important**:  If the block parameter or the `indexSet` is `nil` this method will raise an exception.

 If the block parameter or the `indexSet` is `nil` this method will raise an exception.

## Parameters

- `s`: The indexes of the objects over which to enumerate.
- `opts`: A bit mask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).
- `block`: The block takes three arguments:

## See Also

- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsarray/enumerateobjects(_:).md)
  Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsarray/enumerateobjects(options:using:).md)
  Executes a given closure or block using each object in the array with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/enumerateobjects(at:options:using:))*