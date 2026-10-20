# remove(_:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes the specified object from this object’s array of children.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ object: MDLObject)
```

```objc
- (void) removeObject:(MDLObject *) object;
```

## Parameters

- `object`: The object to remove.

## See Also

### Working with Child Objects
- [var objects: [MDLObject]](./objects.md)
  This object’s array of child objects.
- [func add(MDLObject)](./add%28_%29.md)
  Adds the specified object as a child of this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobjectcontainercomponent/remove(_:))*