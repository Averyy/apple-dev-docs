# objects

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

This object’s array of child objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var objects: [MDLObject] { get }
```

```objc
@property (nonatomic, retain, readonly) NSArray<MDLObject *> * objects;
```

## See Also

### Working with Child Objects
- [func add(MDLObject)](./add%28_%29.md)
  Adds the specified object as a child of this object.
- [func remove(MDLObject)](./remove%28_%29.md)
  Removes the specified object from this object’s array of children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobjectcontainercomponent/objects)*