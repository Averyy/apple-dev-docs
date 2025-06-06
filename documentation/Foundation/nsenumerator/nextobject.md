# nextObject()

**Framework**: Foundation  
**Kind**: method

Returns the next object from the collection being enumerated.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func nextObject() -> Any?
```

#### Return Value

The next object from the collection being enumerated, or `nil` when all objects have been enumerated.

#### Discussion

The following code illustrates how this method works using an array:

```objc
NSArray *anArray = // ... ;
NSEnumerator *enumerator = [anArray objectEnumerator];
id object;
 
while ((object = [enumerator nextObject])) {
    // do something with object...
}
```

## See Also

- [var allObjects: [Any]](nsenumerator/allobjects.md)
  The array of unenumerated objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsenumerator/nextobject())*