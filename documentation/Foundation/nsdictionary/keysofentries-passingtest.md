# keysOfEntries(passingTest:)

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
func keysOfEntries(passingTest predicate: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>
```

#### Return Value

The set of keys whose corresponding value satisfies `predicate`.

## Parameters

- `predicate`: A block object that specifies constraints for values in the dictionary.

## See Also

- [func enumerateKeysAndObjects((Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdictionary/enumeratekeysandobjects(_:).md)
  Applies a given block object to the entries of the dictionary.
- [func keysOfEntries(options: NSEnumerationOptions, passingTest: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsdictionary/keysofentries(options:passingtest:).md)
  Returns the set of keys whose corresponding value satisfies a constraint described by a block object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/keysofentries(passingtest:))*