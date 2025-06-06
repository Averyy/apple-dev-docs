# keysOfEntries(options:passingTest:)

**Framework**: Foundation  
**Kind**: method

Returns the set of keys whose corresponding value satisfies a constraint described by a block object.

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
func keysOfEntries(options opts: NSEnumerationOptions = [], passingTest predicate: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>
```

#### Return Value

The set of keys whose corresponding value satisfies `predicate`.

## Parameters

- `opts`: A bit mask of enumeration options.
- `predicate`: A block object that specifies constraints for values in the dictionary.

## See Also

- [func enumerateKeysAndObjects(options: NSEnumerationOptions, using: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdictionary/enumeratekeysandobjects(options:using:).md)
  Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [func keysOfEntries(passingTest: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsdictionary/keysofentries(passingtest:).md)
  Returns the set of keys whose corresponding value satisfies a constraint described by a block object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/keysofentries(options:passingtest:))*