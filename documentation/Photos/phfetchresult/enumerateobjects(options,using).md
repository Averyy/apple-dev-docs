# enumerateObjects(options:using:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Executes the specified block using each object in the fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func enumerateObjects(options opts: NSEnumerationOptions = [], using block: @escaping (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateObjectsWithOptions:(NSEnumerationOptions) opts usingBlock:(void (^)(ObjectType obj, NSUInteger idx, BOOL *stop)) block;
```

## Discussion

By default, the enumeration starts with the first object and continues in order through the fetch result to the last element specified by the index set. Specify the `concurrent` or `reverse` options to modify this behavior.

This method executes synchronously.

## Parameters

- `opts`: A bit mask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).
- `block`: The block to apply to elements in the fetch result.

  The block takes three parameters:

  - **obj**: The element in the fetch result.
  - **idx**: The index of the element in the fetch result.
  - **stop**: A pointer to a Boolean value. Set `*stop` to `true` within the block to cancel further processing of the fetch result.

## See Also

### Performing Operations with Objects in a Fetch Result
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28at,options,using%29.md)
  Executes the specified block using the objects in the fetch result at the specified indexes.
- [func enumerateObjects((ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateobjects%28_%29.md)
  Executes the specified block using each object in the fetch result, starting with the first object and continuing in order to the last object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult/enumerateobjects(options:using:))*