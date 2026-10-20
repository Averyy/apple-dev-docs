# add(_:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds the specified object as a child of this object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ object: MDLObject)
```

```objc
- (void) addObject:(MDLObject *) object;
```

## Parameters

- `object`: The object to add.

## See Also

### Working with Child Objects
- [var objects: [MDLObject]](./objects.md)
  This object’s array of child objects.
- [func remove(MDLObject)](./remove%28_%29.md)
  Removes the specified object from this object’s array of children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobjectcontainercomponent/add(_:))*