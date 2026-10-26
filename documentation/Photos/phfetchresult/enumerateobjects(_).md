# enumerateObjects(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Executes the specified block using each object in the fetch result, starting with the first object and continuing in order to the last object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func enumerateObjects(_ block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateObjectsUsingBlock:(void (^)(ObjectType obj, NSUInteger idx, BOOL *stop)) block;
```

#### Discussion

This method executes synchronously.

## Parameters

- `block`: The block to apply to elements in the fetch result.

  The block takes three parameters:

  - **obj**: The element in the fetch result.
  - **idx**: The index of the element in the fetch result.
  - **stop**: A pointer to a Boolean value. Set `*stop` to `true` within the block to cancel further processing of the fetch result.

## See Also

### Performing Operations with Objects in a Fetch Result
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28at,options,using%29.md)
  Executes the specified block using the objects in the fetch result at the specified indexes.
- [func enumerateObjects(options: NSEnumerationOptions, using: (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28options,using%29.md)
  Executes the specified block using each object in the fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult/enumerateobjects(_:))*